from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from water.models.client import Client
from water.serialisers.serializer import ClientSerializer
from rest_framework import generics, permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.order_by("-dateCreation").filter(user=self.request.user)

class ClientList(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        self.User = get_object_or_404(User, id=self.kwargs['pk'])
        return Client.objects.filter(user=self.User)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['User'] = self.User
        return context

    

    
    






    