from django.contrib import admin
from .models import Topic, Letter, Product, Content

admin.site.register(Topic, Letter, Product, Content)


