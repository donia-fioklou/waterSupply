from django.urls import path,include
from water.views.client import ClientViewSet
from water.views.dashbord import dashbord
from water.views.distributeur import distributeur,create_distributeur,UpdateDistributeur, distributeur_client_list
from water.views.provision import UpdateProvisionEau, approvisionner_distributeur
from rest_framework import routers
app_name = 'water'

router=routers.SimpleRouter()
router.register('client',ClientViewSet,basename='client')


urlpatterns = [
    path('api/',include(router.urls)),  
    path('dashbord/',dashbord,name='dashbord'),
    path('distributeur/',distributeur,name='distributeur'),
    path('distributeur/create/',create_distributeur,name='create_distributeur'),
    path('distributeur/update/<int:pk>/',UpdateDistributeur.as_view(),name='update_distributeur'),
    path('provisionDis/<int:pk>',approvisionner_distributeur,name="provisionDis"),
    path('provisionDis/update/<int:pk>',UpdateProvisionEau.as_view(),name="update_provisionDis"),
    path('distributeur/client/<int:pk>',distributeur_client_list,name='clientList'),
]