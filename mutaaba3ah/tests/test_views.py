from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

from google.appengine.ext import testbed


class Mutaaba3ahViewsTest(TestCase):

    def setUp(self):
        """Initalise GAE test stubs before each test is run."""

        self.testbed = testbed.Testbed()
        self.testbed.activate()

    def tearDown(self):
        """Remove the GAE test subs after each test."""
        self.testbed.deactivate()

    def test_display_index(self):
        response = self.client.get(reverse('mutaaba3ah'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mutaaba3ah/index.html')

    def test_display_under_construction(self):
        response = self.client.get(reverse('mutaaba3ah/soon'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mutaaba3ah/soon.html')