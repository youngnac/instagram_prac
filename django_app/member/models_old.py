# from django.db import IntegrityError, models
#
#
# class MyUser(models.Model):
#     username = models.CharField('user name', max_length=20, unique=True)
#     last_name = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=20)
#     nickname = models.CharField(max_length=20)
#     email = models.EmailField(blank=False)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)
#     following = models.ManyToManyField('self',
#                                        # on_delete=models.CASCADE(),
#                                        # verbose_name="followers",
#                                        # related_name="followers",
#                                        symmetrical=False,
#                                        blank=True,
#                                        related_name="follower_set"
#                                        )
#
#     def __str__(self):
#         return self.username
#
#     def follow(self, user):
#         self.following.add(user)
#
#     def unfollow(self, user):
#         self.folloing.remove(user)
#
#     @property
#     def followers(self):
#         return self.follwer_set.all()
#
#     def change_nickname(self, new_nickname):
#         self.nickname = new_nickname
#         self.save()
#
#     @staticmethod
#     def create_dummy_user(num):
#         import random
#         last_name_list = ["cho", "lee", "kim", "park"]
#         first_name_list = ["yn", "lk", "sc", "ms"]
#         nickname_list = ["aaa", "bbb", "ccc", "ddd"]
#         created_count = 0
#         for i in range(num):
#             try:
#                 MyUser.objects.create(
#                     username='User{}'.format(i + 1),
#                     last_name=random.choice(last_name_list),
#                     first_name=random.choice(first_name_list),
#                     nickname=random.choice(nickname_list),
#                 )
#                 created_count += 1
#             except IntegrityError as e:
#                 print(e)
#         return created_count
#
#     @staticmethod
#     def allocated_global_variables():
#         # MyUser.allocated_global_variables()
#         import sys
#         module = sys.modules['__main__']
#         users = MyUser.objects.filter(username__startswith='User')
#         for index, user in enumerate(users):
#             # __main__모듈에 u#형태로된 것들을  이름으로 사용해 user로 MyUser객체 할당
#             setattr(module, 'u{}'.format(index + 1), user)
