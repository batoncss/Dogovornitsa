from django.contrib import admin
from .models import Participant, Template


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass



