from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(
    max_length=50,
    unique=True,
    verbose_name=_("Название тега"),
    help_text=_("Введите название тега (максимум 50 символов)"),
    )
    class Meta:
        verbose_name = _("Тег")
        verbose_name_plural = _("Теги")
        ordering = ["name"]
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Исполнитель"))
    pfp = models.ImageField(upload_to="pfps/", null=True)
    major_info = models.TextField(verbose_name="Основная информация")

    class Meta:
        verbose_name = _("Исполнитель")
        verbose_name_plural = _("Исполнители")
        ordering = ["name"]

    def __str__(self):
        return self.name


class VinylRecord(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название альбома"))
    cover = models.ImageField(upload_to="album_covers/", null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artist_name")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    tags = models.ManyToManyField(Tag, related_name="records", blank=True)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(verbose_name=_("Описание альбома"), null=True)

    class Meta:
        verbose_name = _("Винил")
        verbose_name_plural = _("Винилы")
        ordering = ["title"]

    def __str__(self):
        return self.title

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