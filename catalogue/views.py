from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import VinylRecord, Tag, AudioFile, Artist
from django.db.models import Q
from itertools import chain
from icecream import ic
from django.shortcuts import render

class CatalogueView(ListView):
    model = VinylRecord
    template_name = "catalogue.html"
    context_object_name = 'vinyls'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        vinyls_list = VinylRecord.objects.all()

        if query:
            print(query)
            vinyls_list = VinylRecord.objects.filter(
                Q(title__icontains=query) | Q(artist__name__icontains=query)
            )
        return vinyls_list

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.annotate(num_records=models.Count("records")).order_by("-num_records")[:10]
        context['vinyls'] = self.get_queryset()
        return context


class MediaPlayerView(TemplateView):
    model = AudioFile
    template_name = "mp3player.html"
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
        

def VinylView(request, pk):
    vinyl = VinylRecord.objects.get(id=pk)
    return render(request, 'vinyl.html', {'vinyl': vinyl})