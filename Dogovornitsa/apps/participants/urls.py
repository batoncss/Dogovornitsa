from django.urls import path
from .participants_views import participants, participants_delete, participant_detail

urlpatterns = [
    path('', participants, name='participants'),
    path('<int:participant_id>/', participant_detail, name='participant-detail'),
    path('<int:participant_id>/delete/', participants_delete, name='participants-delete'),
]
