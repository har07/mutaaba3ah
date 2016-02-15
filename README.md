
# Mutaaba'ah Yaumiyyah


## Deployment

    $ appcfg.py update ./

If you have two-factor authentication enabled in your Google account, run:

    $ appcfg.py --oauth2 update ./
    
## Running Test

Running specific unit test, for example test_helpers.py :

    python manage.py test mutaaba3ah.tests.test_helpers.Mutaaba3ahHelpersTest.test_group_entries_weekly

