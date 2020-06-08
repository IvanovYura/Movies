from unittest import TestCase

from app import create_app
from service.config import TestConfig

config = TestConfig()


class TestBase(TestCase):
    def setUp(self):
        self.app = create_app(config)
        self.client = self.app.test_client()

    def get(self, url, **kwargs):
        return self.client.get(url, **kwargs)
