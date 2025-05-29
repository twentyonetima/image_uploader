import random
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImageModel
from .serializers import ImageModelSerializer
from django.shortcuts import render


class ImageListView(APIView):
    def get(self, request):
        images = ImageModel.objects.all().order_by('-created_at')
        serializer = ImageModelSerializer(images, many=True)
        return Response(serializer.data)


class ImageUploadView(APIView):
    def post(self, request):
        serializer = ImageModelSerializer(data=request.data)
        if serializer.is_valid():
            image_record = serializer.save()
            time.sleep(2)
            image_record.number = random.randint(1, 1000)
            image_record.save()
            return Response(ImageModelSerializer(image_record).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MassUploadView(APIView):
    def post(self, request):
        file = request.FILES.get('image')
        if not file:
            return Response({'error': 'Image is required'}, status=400)

        results = []
        for _ in range(100):
            instance = ImageModel.objects.create(image=file)
            time.sleep(2)
            instance.number = random.randint(1, 1000)
            instance.save()
            results.append(ImageModelSerializer(instance).data)
        return Response(results, status=201)


def main_view(request):
    return render(request, "main.html")

