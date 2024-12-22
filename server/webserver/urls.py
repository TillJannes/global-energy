from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("energy.urls")),
    path('energy/', include("energy.urls")),
    path('admin/', admin.site.urls),
]
