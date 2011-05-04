===============
django-metadata
===============

With django-metadata you can add data to your instances that are not in the "fields" (which means it is not in a single field at database).

Install
=======

Clone django-metadata and add django-metadata into PYTHONPATH::

  $ export PYTHONPATH=$PYTHONPATH:/somewhere/django-metadata

Remember to replace /somewhere/ to the path where you cloned the code.

You can also add the line above into your ~/.bashrc.

Todo for the future: Release a package to PyPI

Use
===

Import metadata.models.MetaData into your model.py file and create a django.contrib.contenttypes.generic.GenericRelation field where you want to use meta data

Example::

  from django.db import models
  from django.contrib.contenttypes import generic
  from metadata.models import MetaData

  class MyModel(models.Model):
      foo = models.CharField(null=True, blank=True, max_length=1)
      metadata = generic.GenericRelation(MetaData)

Remember to add metadata into your settings.INSTALLED_APPS::

  INSTALLED_APPS = (
    'metadata',
  )

Now syncdb your project to create metadata models and have fun using it::

  from myapp.models import MyModel
  mymodel = MyModel.objects.get(id=1)
  mymodel.metadata.create(name='something', value='some value')
  mymodel.metadata['something']

Note that name and value have a limit of 256 characteres, this is to increase performance and allow any database to index it (PostgreSQL have limit on the size of a VARCHAR field to index it)

MetaData manager objects are dict like objects, and implements __getitem__, __setitem__, iterkeys, keys, itervalues, values, iteritems and items, so you can use them at templates by doing some thing like:

{% if mymodel.metadata.something %}

So it will check if mymodel object has the metadata something into it.

Notes
=====

Please, help the project creating issues, don't be shy :)

This is not a replacement for fields into models, you should use it when some records have some data that other records (in the same table) have not.

Works with Django:

  * 1.0.x
  * 1.1.x
  * 1.2.x
  * 1.3.x
