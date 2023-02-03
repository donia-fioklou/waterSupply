from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import UpdateView
from water.models.distributeur import Distributeur

from water.models.provisionEau import ProvisionEau
def approvisionner_distributeur(request,pk):
    list_provision=ProvisionEau.objects.filter(distributeur_id=pk)
    if request.method=="POST":
        qte=request.POST.get('qte')
        distributeur=Distributeur.objects.get(id=pk)
        
        
        provision_eau= ProvisionEau(qte=qte,distributeur=distributeur)
        provision_eau.save()
    
    return render(request,'water/provisionEau.html',locals())

class UpdateProvisionEau(UpdateView):
    model=ProvisionEau
    template_name='water/provisionEau.html'
    
    def get(self,request,*args, **kwargs):
        provision_eau=get_object_or_404(ProvisionEau,pk=kwargs.get('pk'))
        context = {'provision_eau': provision_eau}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        provision_eau = get_object_or_404(ProvisionEau, pk=kwargs.get('pk'))
        provision_eau.qte = request.POST.get('qte')
        provision_eau.save()
       
        return redirect('/water/provisionDis/')