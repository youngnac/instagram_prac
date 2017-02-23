from django.conf import settings

from member import models
from member.models import MyUser
from post.models.post import Post
from django.db import models


__all__ = (
    'Comment',
)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL )
    post = models.ForeignKey(Post,)
    content = models.CharField(max_length=45)
    created_date = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return "Post [{}]\'s  Comment {} by Author []".format(
            self.post_id,
            self.id,
            self.author.id,
        )
