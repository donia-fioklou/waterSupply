from django.urls import path
from water.views.dashbord import dashbord
app_name = 'water'
urlpatterns = [
path('dashbord/',dashbord,name='dashbord')
]