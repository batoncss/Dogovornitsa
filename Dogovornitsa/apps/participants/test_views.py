from django.test import TestCase, Client
from django.urls import reverse

from .models import Participant


class ViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.unauthorized_client = Client()
        Participant.objects.create(inn="1234567890", name='John')

    # @classmethod
    # def tearDownClass(cls):
    #     super().tearDownClass()

    def test_participant_detail_page(self):
        response = self.unauthorized_client.get(reverse('participant-detail', kwargs={'participant_id': 1}))
        self.assertTrue("<h1>John</h1>" in str(response.content), "Participant name is not available on the page")

    def test_participant_detail_page_fake(self):
        response = self.unauthorized_client.get(reverse('participant-detail', kwargs={'participant_id': 1}))
        self.assertTrue("<h1>John Doe</h1>" in str(response.content), "Participant name is not available on the page")
