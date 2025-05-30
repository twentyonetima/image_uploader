from rest_framework import serializers
from .models import ImageModel
from rest_framework.exceptions import ValidationError

class ImageModelSerializer(serializers.ModelSerializer):
    created_at_formatted = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ImageModel
        fields = ['id', 'image', 'image_url', 'number', 'created_at', 'created_at_formatted']
        read_only_fields = ['number', 'created_at', 'created_at_formatted']

    def get_created_at_formatted(self, obj):
        return obj.created_at.strftime('%d %B %Y, %H:%M:%S')

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def validate_image(self, value):
        if not value.content_type.startswith('image/'):
            raise ValidationError('Файл должен быть изображением.')
        return value