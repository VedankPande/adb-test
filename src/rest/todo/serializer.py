from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    task = serializers.CharField()

