from django.urls import path,include
from water.views.client import ClientCreate, ClientList, ClientUpdate
from water.views.dashbord import dashbord
from water.views.distributeur import user
from water.views.produit import AuthorCreateView, produit_list
from water.views.provision import UpdateProvisionEau, approvisionner_distributeur

app_name = 'water'


urlpatterns = [

    path('dashbord/',dashbord,name='dashbord'),
    path('distributeur/',user,name='distributeur'),
    #path('user/create/',create_user,name='create_user'),
    #path('user/update/<int:pk>/',UpdateDistributeur.as_view(),name='update_user'),
    path('provisionDis/<int:pk>',approvisionner_distributeur,name="provisionDis"),
    path('provisionDis/update/<int:pk>',UpdateProvisionEau.as_view(),name="update_provisionDis"),
    
    #path('client/<int:pk>', ClientList.as_view(), name='client-list'),
    path('client/', ClientList.as_view(), name='client-list'),
    path('client/<int:pk>/update/', ClientUpdate.as_view(), name='client-update'),
    path('client/create/', ClientCreate.as_view(), name='client-create'),
    
    path('produit/',produit_list,name='liste_produit'),
    path('produit/create',AuthorCreateView.as_view(),name='create_produit')
]