from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from post.models import Post
from .forms import LoginForm, SignupForm, ProfileImageForm, SignupForm2


def login_view(request):
    if request.user.is_authenticated:
        return redirect('member:profile')
    else:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/post')
                else:
                    form.add_error(None, 'ID or PW incorrect')
                    # return HttpResponse('Login Failed')
        else:
            form = LoginForm()

        context = {
            'form': form,
        }
        return render(request, 'member/login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.create_user()
            login(request, user)
            return redirect('post:post-list')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


def signup_modelform_view(request):
    if request.method == "POST":
        form = SignupForm2(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post:post-list')
    else:
        form = SignupForm2
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


@login_required
def profile(request):
    user = request.user

    context = {
        'post_count': Post.objects.filter(author=user).count(),
        'follower_count': user.follower_set.count(),
        'following_count': user.following.count(),

    }
    return render(request, 'member/profile.html', context)


@login_required
def change_profile_image(request):
    if request.method == "POST":
        # user = request.user
        # instance로 수정 객체 명시 필
        form = ProfileImageForm(instance=request.user,
                                data=request.POST,
                                files=request.FILES)
        if form.is_valid():
            # file = request.FILES['user_pic']
            # user.user_pic = file
            # user.save()
            form.save(),
            return redirect('member:profile')
    else:
        form = ProfileImageForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'member/profile-pic-add.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('member:login')
