from django.urls import path,include
from water.views.client import ClientList, ClientViewSet
from water.views.dashbord import dashbord
from water.views.distributeur import user
from water.views.produit import  ProduitCreateView, UpdateProduit, produit_list
from water.views.provision import UpdateProvisionEau, approvisionner_distributeur, provision_list

app_name = 'water'


urlpatterns = [

    path('dashbord/',dashbord,name='dashbord'),
    path('distributeur/',user,name='distributeur'),
   
    path('provisionDis/<int:pk>',approvisionner_distributeur,name="provisionDis"),
    path('provisionDis/update/<int:pk>',UpdateProvisionEau.as_view(),name="update_provisionDis"),
    path('distributeur/provision/list/<int:pk>',provision_list,name='provision_list'),
    
    path('distributeur/clients/<int:pk>',ClientList.as_view(),name='distributeur_client_list'),
    
    path('produit/',produit_list,name='liste_produit'),
    path('produit/create',ProduitCreateView.as_view(),name='create_produit'),
    path('produit/update/<int:pk>',UpdateProduit.as_view(),name='update_produit')
]