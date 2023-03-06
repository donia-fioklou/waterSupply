from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage
from water.models.produit import Produit
from water.models.provisionEau import ProvisionEau
from django.contrib import messages


def approvisionner_distributeur(request,pk):
    list_provision=ProvisionEau.objects.filter(user_id=pk)
    paginator= Paginator(list_provision.order_by('-date_prov'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            list_provision=paginator.page(page)
    except EmptyPage:
        list_provision=paginator.page(paginator.num_pages())
    prodQte=Produit.objects.get(id=1).qte
    if request.method=="POST" :
        qte=request.POST.get('qte')
        user=User.objects.get(id=pk) 
        if prodQte < int(qte):
            message="La quantité en stock est insuffisante"
            
        else:     
            provision_eau= ProvisionEau(qte=qte,user=user)
            provision_eau.save()
            return redirect('/water/distributeur/provision/list/'+str(pk))
    
    return render(request,'water/provision_form.html',locals())

def provision_list(request,pk):
    list_provision=ProvisionEau.objects.filter(user_id=pk)
    return render(request,"water/provision.html",locals())

class UpdateProvisionEau(UpdateView):
    model=ProvisionEau
    template_name='water/provision_form.html'
    
    def get(self,request,*args, **kwargs):
        provision_eau=get_object_or_404(ProvisionEau,pk=kwargs.get('pk'))
        context = {'provision_eau': provision_eau}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        provision_eau = get_object_or_404(ProvisionEau, pk=kwargs.get('pk'))
        provision_eau.qte = request.POST.get('qte')
        provision_eau.save()
       
        return redirect('/water/provisionDis/')

