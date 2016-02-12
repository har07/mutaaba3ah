from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

from google.appengine.ext import testbed
from google.appengine.api import users
from google.appengine.datastore import datastore_stub_util

from mutaaba3ah import models

import datetime

class Mutaaba3ahModelsTest(TestCase):
    TEST_USER_EMAIL = 'brian@tester.com'


    def setUp(self):
        """Initalise GAE test stubs before each test is run."""

        self.testbed = testbed.Testbed()
        self.testbed.activate()

        # Create a consistency policy that will simulate the High Replication
        # consistency model.
        self.policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=0)

        #prepare datastore service with the above policy
        self.testbed.init_datastore_v3_stub(consistency_policy=self.policy)
        #create user for test
        self.test_user = User.objects.pre_create_google_user(email=self.TEST_USER_EMAIL)
        # self.user_login()

    def tearDown(self):
        """Remove the GAE test subs after each test."""
        self.testbed.deactivate()

    def user_login(self):
        """
        Set user environment variables and initialize the GAE user stub.
        Taken from http://stackoverflow.com/questions/6159396/.
        """

        self.testbed.setup_env(
            USER_EMAIL=self.TEST_USER_EMAIL,
            USER_ID=self.test_user.id,
            USER_IS_ADMIN='1',
            overwrite=True,
        )
        self.testbed.init_user_stub()

    def test_save_new_entry(self):
        # new_entry = models.Entry.objects.create(owner=self.test_user, entry_date=datetime.datetime.today())
        # user = users.get_current_user()
        # user = self.test_user
        # self.assertEqual(user.email, self.TEST_USER_EMAIL)

        # new_entry = models.Entry()
        # new_entry.owner = user
        # new_entry.entry_date = datetime.datetime.today()
        # new_entry.save()

        models.Entry.objects.create(owner=self.test_user, entry_date=datetime.datetime.today())
        self.assertEqual(1, len(models.Entry.objects.all()))