from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='uploads/')
    number = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image.name} — {self.number}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ['-created_at']