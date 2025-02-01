from django.test import TestCase, Client
from django.urls import reverse

from .models import Participant


class ViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.unauthorized_client = Client()
        cls.participant = Participant.objects.create(
            name='Джонни',
            legal_address='Улица Пушкина, дом Колотушкина',
            actual_address='Улица Лермонтова, дом Неколотушкина',
            inn="123456789012",
            kpp="123456789",
            ogrn="1234567890123"
        )

    def test_participant_detail_page(self):
        response = self.unauthorized_client.get(reverse('participant-detail', kwargs={'participant_id': self.participant.id}))
        self.assertContains(response, "Джонни", msg_prefix="Participant name is not available on the page")
        self.assertContains(response, "Улица Пушкина, дом Колотушкина", msg_prefix="Legal address is not available on the page")
        self.assertContains(response, "Улица Лермонтова, дом Неколотушкина", msg_prefix="Actual address is not available on the page")
        self.assertContains(response, "123456789012", msg_prefix="INN is not available on the page")
        self.assertContains(response, "123456789", msg_prefix="KPP is not available on the page")
        self.assertContains(response, "1234567890123", msg_prefix="OGRN is not available on the page")
