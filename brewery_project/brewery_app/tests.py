from django.test import TestCase
from django.urls import reverse
from .models import Beer

# Create your tests here.
class BeerModelTests(TestCase):
# if beer list object returned
    def index_view_returned(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        beers = response.context['beer_list']  # this is the list of beer
        # check that beers are returned.
        self.assertTrue(beers)

# if index view rendered
class ListBeerListViewTest(TestCase):
    def test_beer_list_view(self): 
        response = self.client.get('index')
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Awesome Brewery</title>', html)  
        self.assertTrue(html.endswith('</html>'))