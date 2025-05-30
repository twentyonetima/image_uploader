from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class YandexS3Storage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    file_overwrite = False

    def _save(self, name, content):
        logger.info(f"Saving file {name} to bucket {self.bucket_name}")
        return super()._save(name, content)