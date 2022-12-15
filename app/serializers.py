from rest_framework import serializers
class NameSerializer(serializers.Serializer):
    email=serializers.EmailField()
    username=serializers.CharField(max_length=10)
    password=serializers.CharField(max_length=100)
