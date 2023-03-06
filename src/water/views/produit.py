from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from water.models.produit import Produit
#from django.core.paginator import Paginator,EmptyPage
from django.views.generic import UpdateView

from django.views.generic.edit import CreateView
from water.models.produit import Produit

class ProduitCreateView(CreateView):
    model = Produit
    fields=["nom","qte"]
    template_name='water/form_produit.html'
    def get_success_url(self):
        return reverse_lazy('water:liste_produit')

def produit_list(request):
    produit_list=Produit.objects.all()
    return render(request,"water/produit.html",locals())

class UpdateProduit(UpdateView):
    model=Produit
    template_name='water/form_produit.html'
    
    def get(self,request,*args, **kwargs):
        produit=get_object_or_404(Produit,pk=kwargs.get('pk'))
        context = {'produit': produit}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        produit = get_object_or_404(Produit, pk=kwargs.get('pk'))
        produit.qte = request.POST.get('qte')
        produit.save()
       
        return redirect('/water/produit/')

