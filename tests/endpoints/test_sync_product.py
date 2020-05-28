from django.test import TestCase, Client


class TestSyncProductEndpoint(TestCase):

    def setUp(self) -> None:
        self.client = Client()
