from django.shortcuts import render
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db.models import Q
from .models import AudioFile
from catalogue.models import VinylRecord, Tag

class MediaPlayerView(TemplateView):
    model = AudioFile
    template_name = "mediaplayer/mp3player.html"
    context_object_name = 'audiofiles'

    def get_queryset(self):
        query = self.request.GET.get("q")
        audiofiles = AudioFile.objects.all()

        if query:
            print(query)
            audiofiles = AudioFile.objects.filter(
                Q(title__icontains=query) | Q(vinyl_record__title__icontains=query)
            )
        return audiofiles

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['audiofiles'] = self.get_queryset()
        context['tags'] = Tag.objects.annotate(num_records=models.Count("records")).order_by("-num_records")[:10]
        context['vinyls'] = VinylRecord.objects.all()
        return context
