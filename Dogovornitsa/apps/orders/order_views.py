from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Dogovornitsa.apps.orders.models import Order


class OrdersView(ListView):
    model = Order
    template_name = "orders/orders.html"
    context_object_name = "object_list"

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('items_per_page', 3)  # По умолчанию 3
        return int(items_per_page)

class OrdersCreateView(CreateView):
    model = Order
    fields = ["name", "body", "template", "participant_1", "participant_2"]
    template_name = "orders/orders-form.html"
    success_url = reverse_lazy("orders")

class OrdersDetailView(DetailView):
    model = Order
    template_name = "orders/orders-detail.html"
    context_object_name = "order"

class OrdersUpdateView(UpdateView):
    model = Order
    fields = ["name", "body", "template", "participant_1", "participant_2"]
    template_name = "orders/orders-form.html"
    success_url = reverse_lazy("orders")

class OrdersDeleteView(DeleteView):
    model = Order
    template_name = "orders/orders-delete.html"
    success_url = reverse_lazy("orders")