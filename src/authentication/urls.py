from django.urls import path
from . import views
app_name = 'authentication'
urlpatterns = [
 # Home page.
 path('login/', views.login_page, name='login'),


 
]