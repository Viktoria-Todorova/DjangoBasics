from django.contrib import messages
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from common.mixins import RecentObjectMixin
from travelers.forms import TravelForm
from travelers.models import Traveler


# Create your views here.

# class TravelerListView(ListView):
#     model = Traveler
#     template_name = 'travelers/traveler_list.html'
#     context_object_name = 'travelers' # This will be the variable name in the template

class TravelerView(CreateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('travelers:traveler_list')

    def form_valid(self, form):
        messages.success(self.request, 'Traveler created successfully')
        return super().form_valid(form)

class TravelerUpdateView(UpdateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('travelers:traveler_list')


class TravelerDeleteView(DeleteView):
    model = Traveler
    success_url = reverse_lazy('travelers:traveler_list')


class TravelerDetailView(DetailView):
    model = Traveler
    # queryset = Traveler.objects.all()    or this
    context_object_name = 'traveler'    #we dont need this because its by default
    def get_context_data(self, **kwargs)->dict:
        context = super().get_context_data()
        context['reviews_count'] = self.object.reviews.count()
        context['visited_destinations'] = self.object.destinations.all()
        return context


class TravelerListView(RecentObjectMixin,ListView):

    paginate_by = 1 #one per page
    ordering = ['-name']

    def get_queryset(self) -> QuerySet[Traveler]:
        qs= Traveler.objects.filter(age__gte=21)
        query= self.request.GET.get('q')

        if query:
            qs= qs.filter(name__icontains=query)

        return qs