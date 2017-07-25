"""
from django.db import models
from django.contrib.contenttypes import generic
from metadata.models import MetaData
import unittest


Deactivated, couldn't make the Test table work

class TestMetaData(models.Model):
    # We need a Model that has a relation to MetaData to test all its features,
    #    so we created one in the test suite. It is not used outside of it 
    foo = models.CharField(null=True, blank=True, max_length=1)
    metadata = generic.GenericRelation(MetaData)

class MetaDataTestCase(unittest.TestCase):
    def testBasic(self):
        test = TestMetaData(foo='b')
        test.save()
        metadata = test.metadata.create(name='twitter_screen_name', value='rafaelsdm')
        metadata = test.metadata.create(name='plurk_user', value='pathiene')

        # Metadata can be used as dict like object (you can't set
        self.assertEqual(test.metadata['twitter_screen_name'], u'rafaelsdm')
        self.assertEqual(test.metadata['plurk_user'], u'pathiene')

        test.metadata['driving'] = 'example'
        self.assertEqual(test.metadata['driving'], u'example')

        # you can also delete entries
        test.metadata.get(name='driving').delete()

        # Always sorted by the name of metadata
        self.assertEqual(test.metadata.keys(), [u'plurk_user', u'twitter_screen_name'])
        self.assertEqual(test.metadata.values(), [u'pathiene', u'rafaelsdm'])

        # You can also iterate over .[iter]items()
        self.assertEqual(test.metadata.items(), [(u'plurk_user', u'pathiene'), (u'twitter_screen_name', u'rafaelsdm')])

        result = []
        for name, value in test.metadata.iteritems():
          result.append([name, value])

        self.assertEqual(result, [[u'plurk_user', u'pathiene'], [u'twitter_screen_name', u'rafaelsdm']])
"""