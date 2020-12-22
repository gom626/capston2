from django.urls import path

from . import views

urlpatterns = [
        path('index/<str:board_id>/', views.index, name='index'),
        #path('<str:room_name>/', views.room, name='room'), # room_name대로

        path('submit/<str:board_id>',views.submit, name='submit'),
]
