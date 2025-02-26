from django.shortcuts import render
from django.db import models
from django.views.generic import TemplateView
from django.db.models import Q
from django.conf import settings
from .models import AudioFile
from catalogue.models import VinylRecord, Tag
from orders.models import OrderItem

class MediaPlayerView(TemplateView):
    model = AudioFile
    template_name = "mediaplayer/mp3player.html"
    context_object_name = 'audiofiles'

    def get_queryset(self):
        if self.request.user.is_authenticated:  # Проверяем, авторизован ли пользователь
            user_orders = OrderItem.objects.filter(order__user=self.request.user)
            vinyls_in_orders = user_orders.values_list('vinyl', flat=True)
            audiofiles = AudioFile.objects.filter(vinyl_record__in=vinyls_in_orders)
        else:
            audiofiles = AudioFile.objects.none()  # Если не авторизован, возвращаем пустой QuerySet

        query = self.request.GET.get("q")
        if query:
            audiofiles = audiofiles.filter(
                Q(title__icontains=query) | Q(vinyl_record__title__icontains=query)
            )
        return audiofiles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BASE_DIR'] = settings.BASE_DIR
        audiofiles = self.get_queryset()
        context['audiofiles'] = audiofiles

        vinyl_ids = audiofiles.values_list('vinyl_record', flat=True).distinct()
        vinyls = VinylRecord.objects.filter(id__in=vinyl_ids)
        context['vinyls'] = vinyls

        return context

# код Ансара ? вроде 

# class MediaPlayerView(LoginRequiredMixin, TemplateView):
#     model = AudioFile
#     template_name = "mediaplayer/mp3player.html"
#     context_object_name = 'audiofiles'

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         user_orders = Order.objects.filter(user=self.request.user, is_completed=True)
#         vinyl_records_in_orders = VinylRecord.objects.filter(orderitem__order__in=user_orders)
#         audiofiles = AudioFile.objects.filter(vinyl_record__in=vinyl_records_in_orders)

#         if query:
#             audiofiles = audiofiles.filter(
#                 Q(title__icontains=query) | Q(vinyl_record__title__icontains=query)
#             )
#         return audiofiles

#     def get_context_data(self, **kwargs: any) -> dict:
#         context = super().get_context_data(**kwargs)
#         context['BASE_DIR'] = settings.BASE_DIR
#         context['audiofiles'] = self.get_queryset()
#         context['tags'] = Tag.objects.annotate(num_records=models.Count("records")).order_by("-num_records")[:10]
#         context['vinyls'] = VinylRecord.objects.all()
#         return context
