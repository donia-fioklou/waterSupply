from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages
from django.views.generic import UpdateView
from water.models.client import Client

from authentication.models import User
def user(request):
    list_user=User.objects.all()
    paginator= Paginator(list_user.order_by('-date_joined'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            list_user=paginator.page(page)
    except EmptyPage:
        list_user=paginator.page(paginator.num_pages())
    return render(request,'water/distributeur.html',locals())
"""
def create_user(request):
    if request.method=="POST":
        nom=request.POST.get('name')
        contact=request.POST.get('contact')
        adresse=request.POST.get('adresse')
        
        user= User(nom=nom,contact=contact,adresse=adresse)
        user.save()
    
    
    return render(request,"water/form_user.html")

class UpdateUser(UpdateView):
    model=User
    template_name='water/form_user.html'
    
    def get(self,request,*args, **kwargs):
        user=get_object_or_404(User,pk=kwargs.get('pk'))
        context = {'user': user}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        user.nom = request.POST.get('nom')
        user.contact = request.POST.get('contact')
        user.adresse = request.POST.get('adresse')
        user.save()
        return redirect('/water/user/')
"""

    
        
        