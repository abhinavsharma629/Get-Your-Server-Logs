from .models import request
from django.db.models import Q
from .models import stats

#FINDING AVERAGE TIME
def findAverageTime(request_type):
	obj=request.objects.filter(Q(currentRequest=request_type))

	totalSecs=0
	for i in obj:
		timeTaken = i.timeToProcess
		timeTaken=str(str(timeTaken).split('.')[0])
		timeParts = [int(s) for s in timeTaken.split(':')]
		totalSecs = totalSecs+ (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
	totalSecs, sec = divmod(totalSecs, 60)
	hr, min = divmod(totalSecs, 60)
	

	total_stats=stats.objects.all()
	for i in total_stats:
		if(request_type=="GET"):
			i.avgResponseTimeGet=("%d:%02d:%02d" % (hr, min, sec))
			i.save()
		elif(request_type=="POST"):
			i.avgResponseTimePost=("%d:%02d:%02d" % (hr, min, sec))
			i.save()
		elif(request_type=="PUT"):
			i.avgResponseTimePut=("%d:%02d:%02d" % (hr, min, sec))
			i.save()
		elif(request_type=="TRACE"):
			i.avgResponseTimeTrace=("%d:%02d:%02d" % (hr, min, sec))
			i.save()
		elif(request_type=="OPTIONS"):
			i.avgResponseTimeOptions=("%d:%02d:%02d" % (hr, min, sec))
			i.save()
		elif(request_type=="DELETE1"):
			i.avgResponseTimeDelete=("%d:%02d:%02d" % (hr, min, sec))
			i.save()
		elif(request_type=="CONNECT"):
			i.avgResponseTimeConnect=("%d:%02d:%02d" % (hr, min, sec))
			i.save()


