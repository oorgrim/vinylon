from django.contrib import admin
from .models import VinylRecord, Tag, Artist

admin.site.register(VinylRecord)
admin.site.register(Tag)
admin.site.register(Artist)
