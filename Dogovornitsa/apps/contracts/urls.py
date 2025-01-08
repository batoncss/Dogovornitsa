from django.urls import path
from .participants_views import participants, participants_delete, participant_detail
from .templates_views import TemplatesView, TemplateView, TemplateCreateView, TemplateUpdateView, TemplateDeleteView

urlpatterns = [
    path('participants/', participants, name='participants'),
    path('participants/<int:participant_id>/', participant_detail, name='participant-detail'),
    path('participants/delete/<int:participant_id>/', participants_delete, name='participants_delete'),
    path('templates/', TemplatesView.as_view(), name='templates'),
    path('templates/create', TemplateCreateView.as_view(), name='template-create'),
    path('templates/<int:pk>/', TemplateView.as_view(), name='template-detail'),
    path('templates/<int:pk>/edit', TemplateUpdateView.as_view(), name='template-edit'),
    path('templates/<int:pk>/delete', TemplateDeleteView.as_view(), name='template-delete'),
]
