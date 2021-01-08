from django.contrib import admin
from .models import Letter, Product, User, Topic

admin.site.register(User)
admin.site.register(Topic)
@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'paper',
        'user',
        'font',
        'month',
        'page',
        'photo_price'
    )
    list_display_links = (
        'paper',
        'user'
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price'
    )




