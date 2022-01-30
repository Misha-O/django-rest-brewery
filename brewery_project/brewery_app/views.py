from rest_framework import viewsets
from django.views import generic

from .models import Beer, Hop, Malt
from .serializers import BeerSerializer
# Create your views here.
class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all().order_by('name')
    serializer_class = BeerSerializer
class IndexView(generic.ListView):
    model = Beer
    template_name = 'brewery_app/index.html'
    context_object_name = 'beer_list'
    ordering = ['-created_at']

class DetailsView(generic.DetailView):
    model = Beer
    template_name = 'brewery_app/detail.html'
    context_object_name = 'beer_list'