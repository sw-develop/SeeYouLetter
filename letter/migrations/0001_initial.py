# Generated by Django 3.0.8 on 2021-01-10 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
                'db_table': 'topics',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderEmail', models.EmailField(max_length=255, verbose_name='email')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20, null=True)),
                ('font', models.CharField(max_length=20, null=True)),
                ('letterContent', models.TextField(blank=True)),
                ('page', models.IntegerField(default=0, null=True)),
                ('photo_price', models.IntegerField(default=0, null=True)),
                ('SelectedQuestions', models.ManyToManyField(blank=True, related_name='letter_topics', to='letter.Topic')),
                ('paper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='letter_paper', to='letter.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='letter_sender', to='letter.User')),
            ],
            options={
                'verbose_name': 'Letter',
                'verbose_name_plural': 'Letters',
                'db_table': 'letters',
                'ordering': ['id'],
                'get_latest_by': 'pk',
            },
        ),
    ]