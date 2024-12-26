from django.shortcuts import render
from django.views.generic import ListView
from catalogue.models import VinylRecord, Tag
# from orders.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count

class HomePageView(ListView):
    model = VinylRecord
    template_name = 'home/home.html'
    context_object_name = 'vinyls'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_tags'] = Tag.objects.annotate(num_records=Count('records')).order_by('-num_records')[:10]
        # if self.request.user.is_authenticated:
        #     context['orders'] = Order.objects.filter(user=self.request.user)
            
        return context
