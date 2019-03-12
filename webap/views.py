from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import request, stats, process
from .serializers import statsSerializer
from django.utils import timezone
from django.db.models import Q
from .requestProcess import requestProcess
from .processingdata import processingdata
from django.http import JsonResponse
import re
import time
import random
import json


#/process
class processList(APIView):
	def get(self,request):
		
		#For Header Elements
		regex_http_          = re.compile(r'^HTTP_.+$')
		regex_content_type   = re.compile(r'^CONTENT_TYPE$')
		regex_content_length = re.compile(r'^CONTENT_LENGTH$')

		request_headers = {}
		for header in request.META:
			if(regex_http_.match(header) or regex_content_type.match(header) or regex_content_length.match(header)):
				request_headers[header] = request.META[header]
		
		#Url Path
		request_path=request.build_absolute_uri(request.path_info)
		
		start_time=timezone.now()
		stime=time.time()

		time.sleep(random.randint(0,1))

		#Data
		data = {
		'time': str(start_time),
		'httpMethod': request.method,
		'httpHeaders':request_headers,
		'requestPath':request_path,
		'queryString': request_path.split('?')[0] if len(request_path.split('?'))==1 else request_path.split('?')[1],
		'requestBody':request.body.decode('utf-8'),
		'timeToProcessRequest':(time.time()-stime)
		}

		#Beautifying Json Data
		try:
			p_json=json.dumps(data)
			parsed_json = json.loads(p_json)
			return HttpResponse(json.dumps(parsed_json, indent = 4,sort_keys=False), content_type="application/json")
		except Exception as e:
			return JsonResponse(data)
		



#/stat
class statList(APIView):
	#GET
	def get(self,request):
		startTime=timezone.localtime(timezone.now())
		processingdata("get")
		commonRequestProcessing()
		requestProcess("GET",startTime)
		return Response(serializer.data)

	#POST
	def post(self, request):
		startTime=timezone.localtime(timezone.now())
		processingdata("post")
		commonRequestProcessing()
		requestProcess("POST",startTime)
		return Response(serializer.data)

	#PUT
	def put(self, request):
		startTime=timezone.localtime(timezone.now())
		processingdata("put")
		commonRequestProcessing()
		requestProcess("PUT",startTime)
		return Response(serializer.data)

	#DELETE
	def delete(self, request):
		startTime=timezone.localtime(timezone.now())
		processingdata("delete")
		commonRequestProcessing()
		requestProcess("DELETE1",startTime)
		return Response(serializer.data)

	#OPTIONS
	def options(self, request):
		startTime=timezone.localtime(timezone.now())
		processingdata("options")
		commonRequestProcessing()
		requestProcess("OPTIONS",startTime)
		return Response(serializer.data)


#CREATING SERIALIZER OBJECT FOR STATS TO RETURN JSON DATA
def commonRequestProcessing():
	global serializer
	total_stats=stats.objects.all()
	serializer= statsSerializer(total_stats, many=True)