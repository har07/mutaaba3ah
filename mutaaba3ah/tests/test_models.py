from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util

from mutaaba3ah import models

import datetime

class Mutaaba3ahModelsTest(TestCase):

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
        self.test_user = User.objects.pre_create_google_user(email='test@example.com')

    def tearDown(self):
        """Remove the GAE test subs after each test."""
        self.testbed.deactivate()

    def test_save_new_entry(self):
        # new_entry = models.Entry.objects.create(owner=self.test_user, entry_date=datetime.datetime.today())
        new_entry = models.Entry()
        new_entry.owner = self.test_user
        new_entry.entry_date = datetime.datetime.today()
        new_entry.save()
        self.assertEqual(1, len(models.Entry.objects.all()))