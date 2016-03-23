from django.test import TestCase
from . import models

class PlatinumCoreViewsTestCases(TestCase):
    def test_index_page(self):
        response = self.client.get('/core/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('num' in response.context)

    def test_league_page(self):
        response = self.client.get('/core/league')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)


# class ModelTests(TestCase):
#     def test_create_player(self):
#         return 0
