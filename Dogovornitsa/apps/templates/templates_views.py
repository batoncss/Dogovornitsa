from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Dogovornitsa.apps.templates.models import Template


class TemplatesView(ListView):
    model = Template
    template_name = "templates/templates.html"
    context_object_name = "object_list"

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('items_per_page', 3)  # По умолчанию 3
        return int(items_per_page)

class TemplatesCreateView(CreateView):
    model = Template
    fields = ["name", "body", "category"]
    template_name = "templates/templates-form.html"
    success_url = reverse_lazy("templates")

class TemplatesDetailView(DetailView):
    model = Template
    template_name = "templates/templates-detail.html"
    context_object_name = "template"

class TemplatesUpdateView(UpdateView):
    model = Template
    fields = ["name", "body", "category"]
    template_name = "templates/templates-form.html"
    success_url = reverse_lazy("templates")

class TemplatesDeleteView(DeleteView):
    model = Template
    template_name = "templates/templates-delete.html"
    success_url = reverse_lazy("templates")