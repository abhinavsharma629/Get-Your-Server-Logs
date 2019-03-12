from .models import stats,request
from django.db.models import Q
from django.utils import timezone
from .checkTime import checkTime

#CREATING / UPDATING STATS MODEL OBJECTS
def processingdata(request_type):
		total_stats = stats.objects.all()

		if(len(total_stats)==0):
			if(request_type=="get"):
				obj,notif=stats.objects.get_or_create(number_of_Requests=1,
					numberOfGet=1, avgResponseTimeGet="00:00:00",getNumberInPastHour=1, getNumberInPastMin=1,
					numberOfPost=0, avgResponseTimePost="00:00:00", postNumberInPastHour=0, postNumberInPastMin=0,
					numberOfPut=0, avgResponseTimePut="00:00:00", putNumberInPastHour=0, putNumberInPastMin=0,
					numberOfDelete=0, avgResponseTimeDelete="00:00:00", deleteNumberInPastHour=0, deleteNumberInPastMin=0,
					numberOfOptions=0, avgResponseTimeOptions="00:00:00", optionsNumberInPastHour=0, optionsNumberInPastMin=0)
			
			elif(request_type=="post"):
				obj,notif=stats.objects.get_or_create(number_of_Requests=1,
					numberOfGet=0, avgResponseTimeGet="00:00:00", getNumberInPastHour=0, getNumberInPastMin=0,
					numberOfPost=1, avgResponseTimePost="00:00:00", postNumberInPastHour=1, postNumberInPastMin=1,
					numberOfPut=0, avgResponseTimePut="00:00:00", putNumberInPastHour=0, putNumberInPastMin=0,
					numberOfDelete=0, avgResponseTimeDelete="00:00:00",deleteNumberInPastHour=0, deleteNumberInPastMin=0,
					numberOfOptions=0, avgResponseTimeOptions="00:00:00", optionsNumberInPastHour=0, optionsNumberInPastMin=0)
			
			elif(request_type=="put"):
				obj,notif=stats.objects.get_or_create(number_of_Requests=1,
					numberOfGet=0, avgResponseTimeGet="00:00:00", getNumberInPastHour=0, getNumberInPastMin=0,
					numberOfPost=0, avgResponseTimePost="00:00:00", postNumberInPastHour=0, postNumberInPastMin=0,
					numberOfPut=1, avgResponseTimePut="00:00:00", putNumberInPastHour=1, putNumberInPastMin=1,
					numberOfDelete=0, avgResponseTimeDelete="00:00:00", deleteNumberInPastHour=0, deleteNumberInPastMin=0,
					numberOfOptions=0, avgResponseTimeOptions="00:00:00", optionsNumberInPastHour=0, optionsNumberInPastMin=0)
			
			elif(request_type=="delete"):
				obj,notif=stats.objects.get_or_create(number_of_Requests=1,
					numberOfGet=0, avgResponseTimeGet="00:00:00", getNumberInPastHour=0, getNumberInPastMin=0,
					numberOfPost=0, avgResponseTimePost="00:00:00", postNumberInPastHour=0, postNumberInPastMin=0,
					numberOfPut=0, avgResponseTimePut="00:00:00", putNumberInPastHour=0, putNumberInPastMin=0,
					numberOfDelete=1, avgResponseTimeDelete="00:00:00", deleteNumberInPastHour=1, deleteNumberInPastMin=1,
					numberOfOptions=0, avgResponseTimeOptions="00:00:00", optionsNumberInPastHour=0, optionsNumberInPastMin=0)
			
			elif(request_type=="options"):
				obj,notif=stats.objects.get_or_create(number_of_Requests=1,
					numberOfGet=0, avgResponseTimeGet="00:00:00", getNumberInPastHour=0, getNumberInPastMin=0, 
					numberOfPost=0, avgResponseTimePost="00:00:00", postNumberInPastHour=0, postNumberInPastMin=0,
					numberOfPut=0, avgResponseTimePut="00:00:00",  putNumberInPastHour=0, putNumberInPastMin=0,
					numberOfDelete=0, avgResponseTimeDelete="00:00:00", deleteNumberInPastHour=0, deleteNumberInPastMin=0,
					numberOfOptions=1, avgResponseTimeOptions="00:00:00", optionsNumberInPastHour=1, optionsNumberInPastMin=1)

			if notif is True:
				obj.save()
		else:
			for i in total_stats:
				i.number_of_Requests=i.number_of_Requests+1
				if(request_type=="get"):
					i.numberOfGet=i.numberOfGet+1
					total=checkTime("GET")
					i.getNumberInPastHour=(int)((total.split('.'))[0])+1
					i.getNumberInPastMin=(int)((total.split('.'))[1])+1

				elif(request_type=="post"):
					i.numberOfPost=i.numberOfPost+1
					total=checkTime("POST")
					i.postNumberInPastHour=(int)((total.split('.'))[0])+1
					i.postNumberInPastMin=(int)((total.split('.'))[1])+1

				elif(request_type=="delete"):
					i.numberOfDelete=i.numberOfDelete+1
					total=checkTime("DELETE1")
					i.deleteNumberInPastHour=(int)((total.split('.'))[0])+1
					i.deleteNumberInPastMin=(int)((total.split('.'))[1])+1

				elif(request_type=="options"):
					i.numberOfOptions=i.numberOfOptions+1
					total=checkTime("OPTIONS")
					i.optionsNumberInPastHour=(int)((total.split('.'))[0])+1
					i.optionsNumberInPastMin=(int)((total.split('.'))[1])+1

				elif(request_type=="put"):
					i.numberOfPut=i.numberOfPut+1
					total=checkTime("PUT")
					i.putNumberInPastHour=(int)((total.split('.'))[0])+1
					i.putNumberInPastMin=(int)((total.split('.'))[1])+1
				i.save()