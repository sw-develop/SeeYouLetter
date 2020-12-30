from django.db import models
from letter.models import Letter
import os

from mysite import settings


class Photo(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')

    def delete(self, *args, **kargs):
        if self.photo:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.path))
        super(Photo, self).delete(*args, **kargs)

    class Meta:
        db_table = 'photos'
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


