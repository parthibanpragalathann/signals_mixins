from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDate
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class HistoryDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryDate
        fields = '__all__'

