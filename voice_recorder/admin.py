from django.contrib import admin
from .models import Record,Author,RecordGroup

admin.site.register(Record)
admin.site.register(RecordGroup)
admin.site.register(Author)
