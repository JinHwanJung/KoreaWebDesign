from django.contrib import admin
from .models import KWD, Category, Color

# Register your models here.
@admin.register(KWD)
class KWDAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_display_links = ['title']

admin.site.register(Category)
admin.site.register(Color)