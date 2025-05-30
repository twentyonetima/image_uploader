import uuid
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImageModel
from .serializers import ImageModelSerializer
from .tasks import process_single_image_task, process_group_image_task


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
            process_single_image_task.delay(image_record.id)
            return Response(ImageModelSerializer(image_record).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MassUploadView(APIView):
    def post(self, request):
        file = request.FILES.get('image')
        if not file:
            return Response({'error': 'Image is required'}, status=400)

        group_id = uuid.uuid4()
        results = []

        instance = ImageModel.objects.create(image=file, group_id=group_id)
        process_group_image_task.delay(instance.id, str(group_id))
        results.append(ImageModelSerializer(instance).data)

        for _ in range(99):
            new_instance = ImageModel.objects.create(image=instance.image.name, group_id=group_id)
            process_group_image_task.delay(new_instance.id, str(group_id))
            results.append(ImageModelSerializer(new_instance).data)

        return Response({
            "message": "100 файлов созданы и отправлены на обработку",
            "group_id": str(group_id),
            "results": results,
        }, status=201)


def main_view(request):
    return render(request, "main.html")