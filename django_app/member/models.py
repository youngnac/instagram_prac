from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.model(username=username)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    CHOICES_GENDER = (
        ('m', 'male'),
        ('f', 'female'),

    )
    username = models.CharField(max_length=25, unique=True)
    nickname = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER)

    following = models.ManyToManyField('self',
                                       through="Relationship",
                                       symmetrical=False,
                                       related_name="follower_set")

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = MyUserManager()
    user_pic = models.ImageField(blank=True, upload_to="member")

    def get_short_name(self):
        return "Hello, {}! Your nickname is {}".format(self.username, self.nickname)

    def get_full_name(self):
        return self.nickname

    def follow(self, user):
        return self.following_relation.create(to_user=user)

    def unfollow(self, user):
        return self.following_relation.get(to_user=user).delete()

    @property
    def followers(self):
        return self.follower_set.all()


#

class Relationship(models.Model):
    from_user = models.ForeignKey(MyUser, related_name="following_relation")
    to_user = models.ForeignKey(MyUser, related_name="followed_by")
    date_follow = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('from_user','to_user',)
        )

    def __str__(self):
        return 'Relation from({}) to ({})'.format(
            self.from_user.username,
            self.to_user.username,
        )


class Model(object):
    pass
