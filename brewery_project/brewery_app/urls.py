from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'beers', views.BeerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'brewery_app'
urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name='index'),
    # ex: /1/
    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),
    # ex: /api/
    path('api/', include(router.urls)),
]
