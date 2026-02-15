from django.db.models import Avg
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from destinations.forms import DestinationForm
from destinations.models import Destination


# Create your views here.

class DestinationCreateView(CreateView):
    model = Destination
    form_class = DestinationForm
    success_url = reverse_lazy('common:home')

class DestinationDetailView(DetailView):

    queryset = Destination.objects.prefetch_related('travelers','reviews').annotate(
        avg_rating=Avg('reviews__rating'),
    )


    #
    # def get_context_data(self, **kwargs) ->dict:
    #     context =super().get_context_data(**kwargs)
    #     context['average_rating'] = self.object.a
    #     return context
