from django.shortcuts import render, redirect

from post.forms import CommentForm
from post.models import Post


def post_list(request):
    context = {
        'post_list': Post.objects.all(),
    }
    return render(request, 'post/post-list.html', context)


# def comment_add(request, author, content ):


def post_detail(request, post_id):
    # if request.method == "POST":
    #     content = request.POST['content']
    #     user = request.user
    #     post = Post.objects.get(id=post_id)
    #     post.add_comment(user, content)
    #     # Comment.objects.create(author=user, post=post, content=content)
    #     return redirect('post:post-detail', post_id=post_id)
    #
    # else:
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
        # 'comment_list': Post.comment_set.all(),

    }
    return render(request, 'post/post-detail.html', context)


def comment_add(request, post_id):
    if request.method == "POST":
        user = request.user
        form = CommentForm(data=request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            post = Post.objects.get(id=post_id)
            post.add_comment(user, content)
            return redirect('post:post-detail', post_id=post_id)
        else:
            post = Post.objects.get(id=post_id)
            context = {
                'post': post
                # 'comment_list': Post.comment_set.all(),

            }

        return render(request, 'post/post-detail.html', context)

        # Comment.objects.create(author=user, post=post, content=content)
        # return redirect('post:post-detail', post_id=post_id)

        # content = request.POST['content']
        # user = request.user
        # post = Post.objects.get(id=post_id)
        # post.add_comment(user, content)
        # # Comment.objects.create(author=user, post=post, content=content)
        # return redirect('post:post-detail', post_id=post_id)
