from django.db import models
from Dogovornitsa.apps.templates.models import Template
from Dogovornitsa.apps.participants.models import Participant

class Order(models.Model):
    name = models.CharField('Наименование договора', max_length=50, unique=True)
    template = models.ForeignKey(
        Template,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Шаблон договора'
    )
    participant_1 = models.ForeignKey(
        Participant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Первый подписант',
        related_name = 'orders_as_participant_1'
    )
    participant_2 = models.ForeignKey(
        Participant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Второй подписант',
        related_name = 'orders_as_participant_2'
    )
    def __str__(self):
        return f"{self.name}"