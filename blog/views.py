from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def home(request):
  blog = BlogPost.objects.all()
  context = {'blog': blog}
  return render(request, template_name='blog/home.html', context=context)