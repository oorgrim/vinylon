from django.db import models
from catalogue.models import Tag, Artist, VinylRecord
from django.utils.translation import gettext_lazy as _


class AudioFile(models.Model):
    vinyl_record = models.ForeignKey(VinylRecord, on_delete=models.CASCADE, related_name="audio_files")
    audio_file = models.FileField(upload_to="vinyl_audio/")
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = _("Трек")
        verbose_name_plural = _("Треки")
        ordering = ["title"]
    
    def __str__(self):
        return self.title