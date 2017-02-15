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
    # since inheriting from AbstractBaseUser
    # password
    # last_loginmg
    # is_active are given

    username = models.CharField(max_length=25, unique=True)
    nickname = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def get_short_name(self):
        return "Hello, {}! Your nickname is {}".format(self.username, self.nickname)
    def get_full_name(self):
        return self.nickname

