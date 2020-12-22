from django.urls import path
from . import views
  
urlpatterns=[
    path('Home/',views.home,name='home'),
    path('Home/dashboard',views.dashboard,name='dashboard')
]

