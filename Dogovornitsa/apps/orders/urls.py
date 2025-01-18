from django.urls import path
from Dogovornitsa.apps.orders.order_views import OrdersView, OrdersCreateView, OrdersDetailView, OrdersUpdateView, OrdersDeleteView

urlpatterns = [
    path('', OrdersView.as_view(), name='orders'),
    path('create/', OrdersCreateView.as_view(), name='orders-create'),
    path('<int:pk>/', OrdersDetailView.as_view(), name='orders-detail'),
    path('<int:pk>/edit', OrdersUpdateView.as_view(), name='orders-edit'),
    path('<int:pk>/delete', OrdersDeleteView.as_view(), name='orders-delete'),
]
