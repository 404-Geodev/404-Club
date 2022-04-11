from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home', include("home.urls", namespace='home')),
    path('admin/', admin.site.urls),
]
