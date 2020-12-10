from django.views.generic import DetailView, ListView

from .models import Rep


class RepListView(ListView):
    model = Rep


class RepDetailView(DetailView):
    model = Rep
