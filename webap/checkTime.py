from .models import stats,request
from django.utils import timezone
from django.db.models import Q

#CHECKING TIME FOR PAST HOUR AND MIN
def checkTime(request_type):
	hourTotal=0
	minTotal=0
	for i in request.objects.filter(Q(currentRequest=request_type)):
		if(((int)(str(timezone.localtime(timezone.now()))[11:13]))-((int)(str(i.creationTime)[0:2]))<=1):
			hourTotal=hourTotal+1
		if(((int)(str(timezone.localtime(timezone.now()))[14:16]))-((int)(str(i.creationTime)[3:5]))<=1):
			minTotal=minTotal+1

	return (str(hourTotal)+"."+str(minTotal))