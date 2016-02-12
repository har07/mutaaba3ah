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
        # self.test_user = User.objects.pre_create_google_user(email='brian@tester.com')
        self.user_login()

    def tearDown(self):
        """Remove the GAE test subs after each test."""
        self.testbed.deactivate()

    def user_login(self):
        """
        Set user environment variables and initialize the GAE user stub.
        Taken from http://stackoverflow.com/questions/6159396/.
        """

        self.testbed.setup_env(
            USER_EMAIL='brian@tester.com',
            USER_ID='12345',
            USER_IS_ADMIN='1',
            overwrite=True,
        )
        self.testbed.init_user_stub()

    def test_display_index(self):
        response = self.client.get(reverse('mutaaba3ah'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mutaaba3ah/create_or_edit_entry.html')

    def test_display_report(self):
        response = self.client.get(reverse('mutaaba3ah/report'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mutaaba3ah/report.html')

    def test_get_report_content(self):
        response = self.client.get(reverse('mutaaba3ah/get_report_content', kwargs={'date_from':'', 'date_to':''}))
        self.assertEqual(response.status_code, 200)
        # self.assertInHTML("report_content", response.body)
        self.assertTemplateUsed(response, 'mutaaba3ah/report_content.html')