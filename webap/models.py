from django.db import models

class request(models.Model):
	REQUESTS=(
		("GET", ("GET")),
		("POST", ("POST")),
		("OPTIONS", ("OPTIONS")),
		("PUT", ("PUT")),
		("DELETE1", ("DELETE1")),
		)
	
	currentRequest=models.CharField(choices=REQUESTS, max_length=10, null=False)
	timeToProcess=models.TimeField()
	creationTime=models.TimeField()


class stats(models.Model):
	number_of_Requests=models.IntegerField()

	numberOfGet=models.IntegerField()
	avgResponseTimeGet=models.TimeField()
	getNumberInPastHour=models.IntegerField()
	getNumberInPastMin=models.IntegerField()

	numberOfPost=models.IntegerField()
	avgResponseTimePost=models.TimeField()
	postNumberInPastHour=models.IntegerField()
	postNumberInPastMin=models.IntegerField()

	numberOfPut=models.IntegerField()
	avgResponseTimePut=models.TimeField()
	putNumberInPastHour=models.IntegerField()
	putNumberInPastMin=models.IntegerField()

	numberOfDelete=models.IntegerField()
	avgResponseTimeDelete=models.TimeField()
	deleteNumberInPastHour=models.IntegerField()
	deleteNumberInPastMin=models.IntegerField()

	numberOfOptions=models.IntegerField()
	avgResponseTimeOptions=models.TimeField()
	optionsNumberInPastHour=models.IntegerField()
	optionsNumberInPastMin=models.IntegerField()

class process(models.Model):
	number_of_Requests=models.IntegerField()