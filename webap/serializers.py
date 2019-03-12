from rest_framework import serializers
from .models import stats

class statsSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=stats  # what module you are going to serialize
		fields= '__all__'