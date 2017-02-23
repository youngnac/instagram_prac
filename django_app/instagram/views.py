from django.shortcuts import redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('post:post-list')
    else:
        return redirect('member:signup')
