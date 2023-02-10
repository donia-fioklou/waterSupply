from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from water.models.client import Client
from water.serialisers.serializer_client import ClientSerializer
from rest_framework import generics, permissions

class ClientCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = permissions.IsAuthenticated

    def perform_create(self):
        data = self.request.data
        client = Client.objects.create(
        user=self.request.user,
        name=data.get('name'),
        email=data.get('email'),
        address=data.get('address')
    )
        
        
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





    