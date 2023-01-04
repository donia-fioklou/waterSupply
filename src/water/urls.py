from django.urls import path
from . import views
app_name = 'water'
urlpatterns = [
 # Home page.
 path('', views.test, name='test'),
]