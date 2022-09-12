from django.urls import path, include
#from rest_framework import routers
#from .views import UserViewSet
from . import views

urlpatterns = [

    path('rooms/', views.room_list),
    path('messages/<str:room>/', views.getMessages),
    path('message/send/', views.sendMssg),
    path('messages/', views.getChats),
    path('messages/post/', views.postChats, name='postchat'),
    path('post/postchat', views.post),


    #path('drf/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]