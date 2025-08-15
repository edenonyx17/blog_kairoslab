#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = UserCreationForm()
    context = {'form': form}
    return render(request, template_name='signup.html', context=context)

