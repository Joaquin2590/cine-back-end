from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_joaquin_rodriguez.urls')),   # la raíz (/) queda en la app
]
