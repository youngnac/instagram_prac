from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from post.forms import CommentForm
from post.models import Post, Comment

__all__ = (
    'comment_add',
    'comment_delete',
)

@login_required
def comment_add(request, post_id):
    if request.method == "POST":
        user = request.user
        form = CommentForm(data=request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            post = Post.objects.get(id=post_id)
            post.add_comment(user, content)
            return redirect('post:post-list')
        else:
            post = Post.objects.get(id=post_id)
            context = {
                'post': post
                # 'comment_list': Post.comment_set.all(),
            }
        return render(request, 'post/post-list.html', context)

@login_required
def comment_delete(request, post_id, comment_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.get(post=post, id=comment_id)
        if comment.author == request.user:
            comment.delete()
        return redirect('post:post-list')
