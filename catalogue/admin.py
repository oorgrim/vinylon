from django.contrib import admin
from .models import VinylRecord, Tag, AudioFile, Artist

admin.site.register(VinylRecord)
admin.site.register(Tag)
admin.site.register(AudioFile)
admin.site.register(Artist)
