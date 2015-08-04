"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import Star

class StarTest(TestCase):
    def setUp(self):
        self.star = Star()
        self.client = Client()
        """Test Client."""

    def test_badge(self):
        """
        Tests to request a badge.
        """
        self.result = self.client.get(reverse('star:options'))
        self.assertEqual(result.status_code, 302)

    def test_demo(self):
        """
        Tests to request the demo page.
        """
        self.result = self.client.get(reverse('star:demo'))
        self.assertEqual(result.status_code, 302)
