from django.test import TestCase
from users.models import GodFather


class GodFatherTestCase(TestCase):
    def setUp(self):
        user = GodFather.objects.create(**{
            'email': 'jdoe@example.com',
            'firt_name': 'john',
            'last_name': 'doe',
            'password': 'test123',
            'country': '',
            'state': '',
        })
