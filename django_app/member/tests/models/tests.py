from django.db import IntegrityError
from django.test import TransactionTestCase

from utils.test import make_dummy_users


class MyUserModelTest(TransactionTestCase):
    def test_following(self):
        ul = make_dummy_users()
        ul[0].follow(ul[1])
        ul[0].follow(ul[2])
        ul[0].follow(ul[3])

        ul[1].follow(ul[2])
        ul[1].follow(ul[3])

        ul[2].follow(ul[3])
        ul[2].follow(ul[4])

        self.assertIn(ul[1], ul[0].following.all())
        self.assertIn(ul[2], ul[0].following.all())
        self.assertIn(ul[3], ul[0].following.all())

        self.assertIn(ul[0], ul[1].follower_set.all())
        self.assertIn(ul[0], ul[2].follower_set.all())
        self.assertIn(ul[0], ul[3].follower_set.all())

        self.assertIn(ul[2], ul[1].following.all())
        self.assertIn(ul[3], ul[1].following.all())

        self.assertIn(ul[1], ul[2].follower_set.all())
        self.assertIn(ul[1], ul[3].follower_set.all())

        self.assertIn(ul[3], ul[2].following.all())
        self.assertIn(ul[4], ul[2].following.all())

        self.assertIn(ul[2], ul[3].follower_set.all())
        self.assertIn(ul[2], ul[4].follower_set.all())

    def test_following_duplicate(self):
        ul = make_dummy_users()
        ul[0].follow(ul[1])

        # 중복 팔로우 시도를 위해...
        with self.assertRaises(IntegrityError):
            ul[0].follow(ul[1])

        self.assertEqual(
            ul[0].following_relation.filter(to_user=ul[1]).count(),
            1)
        self.assertEqual(ul[1].follower_set.count(), 1)
        # self.assertEqual(ul[0].following_relation.filter(to_user=ul[1]).count(), 1)

    def test_unfollow(self):
        ul = make_dummy_users()
        ul[0].follow(ul[1])
        ul[0].follow(ul[2])
        ul[0].follow(ul[3])

        ul[0].unfollow(ul[1])
        self.assertEqual(ul[0].following.count(), 2)
        ul[0].unfollow(ul[2])
        self.assertEqual(ul[0].following.count(), 1)
        ul[0].unfollow(ul[3])
        self.assertEqual(ul[0].following.count(), 0)
