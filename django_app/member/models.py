from django.db import IntegrityError, models


class MyUser(models.Model):
    username = models.CharField('user name', max_length=20, unique=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    email = models.EmailField(blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    following = models.ManyToManyField('self',
                                       # on_delete=models.CASCADE(),
                                       # verbose_name="followers",
                                       # related_name="followers",
                                       symmetrical=False,
                                       blank=True
                                       )

    def __str__(self):
        return self.username

    @staticmethod
    def create_dummy_user(num):
        import random
        last_name_list = ["cho", "lee", "kim", "park"]
        first_name_list = ["yn", "lk", "sc", "ms"]
        nickname_list = ["aaa", "bbb", "ccc", "ddd"]
        created_count = 0
        for i in range(num):
            try:
                MyUser.objects.create(
                    username='User{}'.format(i + 1),
                    last_name=random.choice(last_name_list),
                    first_name=random.choice(first_name_list),
                    nickname=random.choice(nickname_list),
                )
                created_count += 1
            except IntegrityError as e:
                print(e)
        return created_count

    @staticmethod
    def allocated_global_variables():
        for i in ranage(num):
