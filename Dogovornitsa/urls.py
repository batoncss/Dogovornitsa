from django.contrib import admin
from django.urls import path, include
from Dogovornitsa.views import templates_home

urlpatterns = [
    path('', templates_home, name='home'),
    path('admin/', admin.site.urls),
    path('participants/', include('participants.urls')),
    path('templates/', include('templates.urls')),
    path('orders/', include('orders.urls')),
]
