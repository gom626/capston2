from django.urls import path
from . import views
  
urlpatterns = [

    path('create/',views.create,name='create'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('createPost/', views.createPost, name='createPost'),
    path('category/<str:game>/',views.category, name='category'),
    path('regist/<int:blog_id>/',views.regist, name='regist'),
]

