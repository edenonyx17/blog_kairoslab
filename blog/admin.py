from django.contrib import admin
from .models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'author', 'body', 'date_created']

  def save_model(self, request, obj, form, change):
    obj.author = request.user
    super().save_model(request, obj, form, change)

admin.site.register(BlogPost, BlogPostAdmin)