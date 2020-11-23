from django.contrib import admin
from .models import Artist 

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
    )
    ordering = ('name',)

admin.site.register(Artist, ArtistAdmin)
