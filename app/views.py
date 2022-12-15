from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from app import serializers
from app.models import *


class SampleViewset(viewsets.ViewSet):
    serializer_class=serializers.NameSerializer
    def list(self,request):
        data=UserProfile.objects.values()
        return Response({'data':data})
    def create(self,request):
        data=self.serializer_class(data=request.data)
        if data.is_valid():
            email=data._validated_data.get('email')
            username=data.validated_data.get("username")
            password=data.validated_data.get('password')
            u=UserProfile.objects.get_or_create(email=email,first_name=username)[0]
            u.set_password(password)
            u.is_staff=True
            u.is_superuser=True
            u.save()
            return Response({'message':"user is created successfully"})
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        return Response({'data':UserProfile.objects.filter(id=pk).values()})
    

