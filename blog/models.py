from django.db import models

# Create your models here.
class BlogPost(models.Model):
  title = models.CharField(max_length=180)
  author = models.CharField(max_length=50)
  body = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
