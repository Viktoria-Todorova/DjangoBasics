from typing import List

from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView, RedirectView

from travelers.models import Traveler


class WelcomeView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return HttpResponse(status=403)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('Welcome to our travel App!')

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('Post was called')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # format datetime as "YYYY-MM-DD HH:MM:SS"
        kwargs.update({'travelers_count': Traveler.objects.count(),
                       'current_time': now()},
                      )
        # context["current_time"] = now().strftime("%Y-%m-%d %H:%M:%S")
        return context

    def get_template_names(self) -> List[str]:
        if self.request.user.is_staff:
            return ['admin_home.html']
        return ['home.html']


class HomeTeenView(TemplateView):
    template_name = 'teen-welcome.html'


class AgeCheckRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs) -> str:
        pk = self.request.GET.get('pk')
        traveler = get_object_or_404(Traveler, pk=pk)

        # safe redirects to template views (no further redirects)
        if traveler.age > 21:
            return reverse('common:home-teen')
        return reverse('common:home')
