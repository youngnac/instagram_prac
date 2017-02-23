from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from post.forms import CommentForm, PostForm
from post.models import Post

__all__ = (
    'post_list',
    'post_detail',
    'post_like_toggle',
    'post_delete',
    'post_add',
)


def post_list(request):
    context = {
        'post_list': Post.objects.filter(is_visible=True)
    }
    # if form

    return render(request, 'post/post-list.html', context)


# def comment_add(request, author, content ):


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
        # 'comment_list': Post.comment_set.all(),

    }

    return render(request, 'post/post-detail.html', context)

@login_required
def post_like_toggle(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.toggle_like(user=request.user)
        # return redirect('post:post-detail', post_id=post_id)
        return redirect('post:post-list')

@login_required
def post_delete(request, post_id, db_delete=False):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        if request.user.id == post.author.id:
            if db_delete:
                post.delete()
            else:
                post.is_visible = False
                post.save()
                # post.delete()
        return redirect('post:post-list')

@login_required
def post_add(request):
    user = request.user

    def create_post_comment_from_data(file, comment_content):
        post = Post(author=user, photo=file)
        post.save()
        if comment_content.strip() != '':
            post.add_comment(user, comment_content)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('photo')
            comment_content = form.cleaned_data.get('content', '')
            for file in files:
                create_post_comment_from_data(file, comment_content)

            return redirect('post:post-list')
    else:
        form = PostForm()
    context = {
        'form': form
    }

    return render(request, 'post/post-add.html', context)
