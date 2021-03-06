from django.conf import settings
from django.db import models

from member.models import MyUser

__all__ = (
    'Post',
    'PostLike',
)


class PostManager(models.Manager):
    def visible(self):
        return super().get_queryset().filter(is_visible=True)


class PostUserVisibleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_visible=True)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField('Profile Picture', blank=True, upload_to="post")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        through="PostLike",
                                        # through_fields=("user", "post"),
                                        related_name="like_post_set"
                                        )
    # like_post_set: user에서 like한  post 볼때
    # content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    objects = PostManager()
    visibles = PostUserVisibleManager()

    def __str__(self):
        return 'Post [{}]'.format(self.id)

    class Meta:
        ordering = ('-id',)

    def toggle_like(self, user):
        pl_list = PostLike.objects.filter(post=self, user=user)
        PostLike.objects.create(post=self, user=user) if not pl_list.exists() else pl_list.delete()
        # pl_list.delete() if pl_list.exists() else PostLike.objects.create(post=self, user=user)

        # 현재 인자로 전달된 user가 해당 post를 like한 적이 있는지 검사
        # if pl_list.exists():
        #     # 햇을 경우 삭제 remove/add 사용불가 중간자 사용했기때문에
        #     pl_list.delete()
        # else:
        #     # 없을 경우 생성
        #     PostLike.objects.create(post=self, user=user)

    def add_comment(self, user, new_comment):
        return self.comment_set.create(
            author=user,
            content=new_comment
        )

    @property
    def like_count(self):
        return self.like_users.count()

    @property
    def comment_count(self):
        # post에서 Comment
        return self.comment_set.count()


# intermediary btw MyUser and Post
class PostLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 한 user가 post를 한번만 like하도록 (중복으로 like 불가하게
        unique_together = (
            ('user', 'post')
        )

    def __str__(self):
        return "Post {}\'s Like {} ".format(
            self.post_id,
            self.id,
        )
