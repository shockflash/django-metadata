from metadata.models import MetaData
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

class MetaDataTabularInline(GenericTabularInline):
    model = MetaData
    
class MetaDataStackedInline(GenericStackedInline):
    model = MetaData