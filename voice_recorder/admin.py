from django.contrib import admin
from .models import Record,Doctor,RecordGroup

admin.site.register(Record)
admin.site.register(RecordGroup)
admin.site.register(Doctor)
