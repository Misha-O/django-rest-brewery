from django.contrib import admin
from .models import Beer, Water, Hop, Malt


class WaterInline(admin.TabularInline):
    model = Water
class HopInline(admin.TabularInline):
    model = Hop
class MaltInline(admin.TabularInline):
    model = Malt

class BeerAdmin(admin.ModelAdmin):
    inlines = [
        WaterInline, HopInline, MaltInline
    ]
    search_fields = ['name']

# Register your models here.
admin.site.register(Beer, BeerAdmin)