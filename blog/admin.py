from django.contrib import admin
from . import models

# Register your models here.

# admin.site.register(models.BlogPost)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(models.BlogPost, BlogPostAdmin)