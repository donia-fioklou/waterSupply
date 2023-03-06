from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages
from django.views.generic import UpdateView
from water.models.client import Client

from django.contrib.auth.models import User
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

    
        
        