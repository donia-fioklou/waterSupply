from django.urls import path
from water.views.dashbord import dashbord
from water.views.distributeur import distributeur,create_distributeur,UpdateDistributeur
from water.views.provision import approvisionner_distributeur
app_name = 'water'
urlpatterns = [
    path('dashbord/',dashbord,name='dashbord'),
    path('distributeur/',distributeur,name='distributeur'),
    path('distributeur/create/',create_distributeur,name='create_distributeur'),
    path('distributeur/update/<int:pk>/',UpdateDistributeur.as_view(),name='update_distributeur'),

    path('provisionDis/',approvisionner_distributeur,name="provisionDis")
]