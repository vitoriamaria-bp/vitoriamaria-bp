from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Redireciona tudo para as rotas do freelacademy
    path('', include('freelacademy.urls')), 
]