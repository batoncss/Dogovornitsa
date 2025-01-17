from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('participants/', include('participants.urls')),
    path('templates/', include('templates.urls')),
    path('orders/', include('orders.urls')),
    path('', include('pages.urls')),
]
