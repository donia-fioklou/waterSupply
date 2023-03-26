from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from water.models.commande import Commande
from water.serialisers.serializer import ApprovisonnerSerializer, CommandeSerializer
from rest_framework import generics, permissions,status
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class CommandeViewSet(ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CommandeList(LoginRequiredMixin,ListView):
    login_url='/login/'
    model = Commande
    template_name = 'client/commande_list.html'
    context_object_name = 'commandes'

    def get_queryset(self):
        self.User = get_object_or_404(User, id=self.kwargs['pk'])
        return Commande.objects.filter(user=self.User)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['User'] = self.User
        return context


class Approvisionner(generics.UpdateAPIView):
    queryset = Commande.objects.all()
    serializer_class = ApprovisonnerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


        
  