from django.db import models 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import VinylRecord, Tag, Artist
from django.db.models import Q
from itertools import chain
from icecream import ic
from django.shortcuts import render
from .serializers import VinylRecordSerializer
from rest_framework import generics
from orders.models import OrderItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CatalogueView(ListView):
    model = VinylRecord
    template_name = "catalogue/catalogue.html"
    context_object_name = 'vinyls'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        vinyls_list = VinylRecord.objects.all()

        if query:
            vinyls_list = VinylRecord.objects.filter(
                Q(title__icontains=query) | Q(artist__name__icontains=query)
            )
        return vinyls_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.annotate(num_records=models.Count("records")).order_by("-num_records")[:10]
        context['vinyls'] = self.get_queryset()

        if self.request.user.is_authenticated:
            user_orders = OrderItem.objects.filter(order__user=self.request.user)
            vinyls_in_orders = user_orders.values_list('vinyl', flat=True)
            user_ordered_vinyls = VinylRecord.objects.filter(id__in=vinyls_in_orders)
            context['your_songs'] = user_ordered_vinyls
        else:
            context['your_songs'] = []

        return context


class VinylDetail(DetailView):
    model = VinylRecord
    template_name = "catalogue/vinyl.html"
    success_url = reverse_lazy("cart:cart_summary")

    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['vinyl'] = self.get_object()
        context['vinyls'] = VinylRecord.objects.all()[:10]
        return context


class TagListAPIView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = VinylRecordSerializer(tags, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = VinylRecordSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = VinylRecordSerializer  


def catalogue_view(request):
    if request.user.is_authenticated:
        user_orders = OrderItem.objects.filter(order__user=request.user)
        vinyls_in_orders = user_orders.values_list('vinyl', flat=True)
        vinyls = VinylRecord.objects.filter(id__in=vinyls_in_orders)
    else:
        vinyls = VinylRecord.objects.none()

    return render(request, 'catalogue/catalogue.html', {'vinyls': vinyls})