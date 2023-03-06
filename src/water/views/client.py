from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from water.models.client import Client
from water.serialisers.serializer_client import ClientSerializer
from rest_framework import generics, permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        data = request.data
        data['user'] = user
        serializer.save(**data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ClientUpdate(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


    
    






    