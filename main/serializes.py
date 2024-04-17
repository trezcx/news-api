from rest_framework import serializers
from .models import News, Application

class ApplictaionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'