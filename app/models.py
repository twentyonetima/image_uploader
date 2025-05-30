from django.db import models
from services.yandex_s3_storage import YandexS3Storage

class ImageModel(models.Model):
    image = models.ImageField(storage=YandexS3Storage())
    number = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    group_id = models.UUIDField(null=True, blank=True)

    def __str__(self):
        return f"{self.image.name} — {self.number}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ['-created_at']