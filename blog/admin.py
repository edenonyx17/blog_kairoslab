from django.contrib import admin
from .models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'author', 'body', 'date_created']

admin.site.register(BlogPost, BlogPostAdmin)