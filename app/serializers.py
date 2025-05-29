from rest_framework import serializers
from .models import ImageModel

class ImageModelSerializer(serializers.ModelSerializer):
    created_at_formatted = serializers.SerializerMethodField()

    class Meta:
        model = ImageModel
        fields = ['id', 'image', 'number', 'created_at', 'created_at_formatted']
        read_only_fields = ['number', 'created_at', 'created_at_formatted']

    def get_created_at_formatted(self, obj):
        return obj.created_at.strftime('%d %B %Y, %H:%M:%S')