from django.contrib import admin
from django.urls import path, include

from apps.core import urls as urls_core


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls_core)),
]
