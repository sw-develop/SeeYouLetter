from django.db import models
from letter.models import Letter

class Photo(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')

    class Meta:
        db_table = 'photos'
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


