from django.urls import path
from . import views
app_name = 'authentication'
urlpatterns = [
 # Home page.
 path('', views.login_page, name='login'),


 
]