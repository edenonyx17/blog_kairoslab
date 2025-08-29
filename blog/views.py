from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def home(request):
    """Return the list of blogposts."""
    blog = BlogPost.objects.all()
    context = {'blog': blog}
    return render(request, template_name='blog/home.html', context=context)

@login_required
def blog_detail(request, blog_id):
    """Detail of a blog post."""
    blog = get_object_or_404(BlogPost, id=blog_id)
    #blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, template_name='blog/blog_detail.html', context=context)

@login_required
def create_blog(request):
    """Create a blog post"""
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

#@login_required
def update_blog(request, blog_id):
    """Update a blog."""
    blog = get_object_or_404(BlogPost, id=blog_id)
    print(request.user)
    if blog.author != request.user:
        raise Http404

    if request.method == 'POST':
        form = BlogForm(data=request.POST, instance=blog)
        if form.is_valid():
            edited_blog = form.save(commit=False)
            #edited_blog.author = request.user
            edited_blog.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        context = {'form': form}
        return render(request, 'blog/update_blog.html', context=context)

@login_required
def delete_blog(request, blog_id):
    """Delete a blog."""
    blog = get_object_or_404(BlogPost, id=blog_id)
    #if request.user ==
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    else:
        context = {'blog': blog}
        return render(request, template_name='blog/delete_blog.html', context=context)


def about(request):
    return render(request, template_name='blog/about.html')