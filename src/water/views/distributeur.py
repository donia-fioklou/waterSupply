from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.views.generic import UpdateView

from water.models.distributeur import Distributeur
def distributeur(request):
    list_distributeur=Distributeur.objects.all()
    return render(request,'water/distributeur.html',context={'list_distributeur':list_distributeur})

def create_distributeur(request):
    if request.method=="POST":
        nom=request.POST.get('name')
        contact=request.POST.get('contact')
        adresse=request.POST.get('adresse')
        
        distributeur= Distributeur(nom=nom,contact=contact,adresse=adresse)
        distributeur.save()
    
    return render(request,"water/form_distributeur.html")

class UpdateDistributeur(UpdateView):
    model=Distributeur
    template_name='water/form_distributeur.html'
    
    def get(self,request,*args, **kwargs):
        distributeur=get_object_or_404(Distributeur,pk=kwargs.get('pk'))
        context = {'distributeur': distributeur}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        distributeur = get_object_or_404(Distributeur, pk=kwargs.get('pk'))
        distributeur.nom = request.POST.get('nom')
        distributeur.contact = request.POST.get('contact')
        distributeur.adresse = request.POST.get('adresse')
        distributeur.save()
        return redirect('/water/distributeur/')
        
        