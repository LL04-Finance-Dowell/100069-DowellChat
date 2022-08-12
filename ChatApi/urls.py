from django.urls import path, include
from rest_framework import routers
#from .views import UserViewSet
from .views import room_list, getMessages, sendMssg

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

urlpatterns = [

    path('rooms/', room_list),
    path('messages/<str:room>/', getMessages),
    path('message/send/', sendMssg),

    #path('drf/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]