from django.urls import path
from .views import main_view, ImageUploadView, ImageListView, MassUploadView

urlpatterns = [
    path("", main_view, name="main"),
    path('api/upload/', ImageUploadView.as_view(), name='upload-image'),
    path('api/list/', ImageListView.as_view(), name='image-list'),
    path('api/mass-upload/', MassUploadView.as_view(), name='mass-upload'),
]