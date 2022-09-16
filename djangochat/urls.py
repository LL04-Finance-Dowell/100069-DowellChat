from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('api/', include('ChatApi.urls')),
    #path('create-room/', include('chat.urls')),
    
    path('productsapi/', include('productsApi.urls')),
    path('chat/', include('dowellchat.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)