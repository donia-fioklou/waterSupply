from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from water.models.client import Client
from water.serialisers.serializer import ClientSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.order_by("-dateCreation").filter(user=self.request.user)

class ClientList(LoginRequiredMixin,ListView):
    login_url='/login/'
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



    

    
    






    