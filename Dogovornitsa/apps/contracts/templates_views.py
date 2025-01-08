from django.urls import reverse_lazy
from django.views.generic import TemplateView as TemplateGenericView, ListView, DetailView, CreateView, UpdateView, \
    DeleteView

from Dogovornitsa.apps.contracts.models import Template


# class TemplatesView(TemplateGenericView):
#     template_name = "contracts/templates.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['templates'] = Template.objects.all()
#         return context


class TemplatesView(ListView):
    model = Template
    template_name = 'contracts/templates.html'
    # todo: make pagination
    # context_object_name = 'templates'

class TemplateView(DetailView):
    model = Template
    template_name = 'contracts/template-detail.html'

class TemplateCreateView(CreateView):
    model = Template
    fields = ["name", "body"]
    template_name = "contracts/template-form.html"  # Укажите свой шаблон
    success_url = reverse_lazy("templates")

class TemplateUpdateView(UpdateView):
    model = Template
    fields = ["name", "body"]
    template_name = "contracts/template-form.html"
    success_url = reverse_lazy("templates")

class TemplateDeleteView(DeleteView):
    model = Template
    template_name = "contracts/template-delete.html"
    success_url = reverse_lazy("templates")
