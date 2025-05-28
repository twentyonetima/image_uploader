from django.contrib import admin
from .models import ImageModel

@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('number',)
    ordering = ('-created_at',)
