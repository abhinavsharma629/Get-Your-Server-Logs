from .models import request
from django.utils import timezone
from .findAverageTime import findAverageTime

#CREATING REQUEST OBJECT
def requestProcess(request_type,startTime):
	endTime=timezone.localtime(timezone.now())
	timeTaken=endTime-startTime
	print(str(timeTaken))
	obj,notif=request.objects.get_or_create(currentRequest=request_type, timeToProcess=str(timeTaken), creationTime=startTime)
	if notif is True:
		obj.save()
	#print(obj, request.objects.all())
	findAverageTime(request_type)