from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogForm
from .models import BlogPost

# Create your views here.
def home(request):
  blog = BlogPost.objects.all()
  context = {'blog': blog}
  return render(request, template_name='blog/home.html', context=context)


def blog_detail(request, blog_id):
  """Detail of the blog"""
  blog = get_object_or_404(BlogPost, id=blog_id)
  context = {'blog': blog}
  return render(request, template_name='blog/blog_detail.html', context=context)

def create_blog(request):
  if request.method == 'POST':
    form = BlogForm(data=request.POST)
    if form.is_valid():
      new_blog = form.save(commit=False)
      new_blog.author = request.user
      new_blog.save()
      return redirect('home')
  else:
    form = BlogForm()
    context = {'form': form}
    return render(request, template_name='blog/create_blog.html', context=context)

def update_blog(request, blog_id):
  blog = get_object_or_404(BlogPost, id=blog_id)
  if request.method == 'POST':
    form = BlogForm(data=request.POST, instance=blog)
    if form.is_valid():
      edited_blog = form.save(commit=False)
      if not edited_blog.author:
        edited_blog.author = request.user
      edited_blog.author = request.user
      edited_blog.save()
      return redirect('home')
  else:
    form = BlogForm(instance=blog)
    context = {'form': form}
    return render(request, template_name='blog/update_blog.html', context=context)

def delete_blog(request, blog_id):
  blog = get_object_or_404(BlogPost, id=blog_id)
  if request.method == 'POST':
    blog.delete()
    return redirect('home')
  else:
    context = {'blog': blog}
    return render(request, template_name='blog/delete_blog.html', context=context)

