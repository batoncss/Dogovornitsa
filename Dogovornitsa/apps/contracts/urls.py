from django.urls import path
from .views import participants, participants_delete, participant_detail


urlpatterns = [
    path('participants', participants, name='participants'),
    path('participants/<int:participant_id>/', participant_detail, name='participant-detail'),
    path('participants/delete/<int:participant_id>/', participants_delete, name='participants_delete'),
]
