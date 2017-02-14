from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin')
            else:
                form.add_error(None,'ID or PW incorrect')
                # return HttpResponse('Login Failed')
    else:
        form = LoginForm()

    context = {
        'form': form,
        }
    return render(request, 'member/login.html', context)
