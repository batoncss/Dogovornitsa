from django.urls import path
from  .views import making_order, home, templates


urlpatterns = [
    path('', home, name='home'),
    path('making-order/', making_order, name='makingOrder'),
    path('templates/', templates, name='templates'),
]
