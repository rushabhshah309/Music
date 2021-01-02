from django.views import generic
from .models import *


class IndexView(generic.ListView):
    template_name = "app1/index.html"
    context_object_name = 'allAlbums'

    def get_queryset(self):
        return Albums.objects.all()


class DetailView(generic.DetailView):
    model = Albums
    context_object_name = 'albums_details'
    template_name = "app1/details.html"

