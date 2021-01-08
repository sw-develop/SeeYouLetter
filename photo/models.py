from django.db import models
from letter.models import Letter
import os
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

from mysite import settings


class Photo(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image_url = models.URLField(null=True)

    def delete(self, *args, **kargs):
        if self.photo:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.path))
        super(Photo, self).delete(*args, **kargs)

    def get_remote_image(self):
        if self.image_url and not self.photo:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.photo.save(f"image_{self.pk}", File(img_temp))
        self.save()

    class Meta:
        db_table = 'photos'
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        get_latest_by = 'pk'
        ordering =['id']


