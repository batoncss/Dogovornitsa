from django.urls import path
from Dogovornitsa.apps.templates.templates_views import TemplatesView, TemplatesCreateView, TemplatesUpdateView, TemplatesDeleteView, TemplatesDetailView

urlpatterns = [
    path('', TemplatesView.as_view(), name='templates'),
    path('create/', TemplatesCreateView.as_view(), name='template-create'),
    path('<int:pk>/', TemplatesDetailView.as_view(), name='template-detail'),
    path('<int:pk>/edit', TemplatesUpdateView.as_view(), name='template-edit'),
    path('<int:pk>/delete', TemplatesDeleteView.as_view(), name='template-delete'),
]
