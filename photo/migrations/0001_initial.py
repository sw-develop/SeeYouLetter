# Generated by Django 3.0.8 on 2021-01-07 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('letter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='photos/no_image.png', upload_to='photos/%Y/%m/%d')),
                ('image_url', models.URLField()),
                ('letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_photos', to='letter.Letter')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'db_table': 'photos',
            },
        ),
    ]