import random

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from member.models import MyUser
from post.models import Post
from utils.test import make_dummy_users


class BaseTestUser(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def make_url(self, url):
        return self.live_server_url + url

    def make_user_and_login(self):
        test_username = "test_user"
        test_password = "test_password"
        user = MyUser.objects.create_user(test_username, test_password)

        self.browser.get(self.live_server_url + '/member/login/')
        input_username = self.browser.find_element_by_name('username')
        input_username.send_keys(test_username)

        input_password = self.browser.find_element_by_name('password')
        input_password.send_keys(test_password)

        input_password.send_keys(Keys.ENTER)

        return user


class TestIndexDirect(BaseTestUser):
    def test_new_visitor(self):
        self.browser.get(self.live_server_url)

        self.assertEqual(self.live_server_url + '/member/signup/', self.browser.current_url)

    def test_logged_in_user(self):
        test_username = "test_user"
        test_password = "test_password"
        MyUser.objects.create_user(test_username, test_password)

        self.browser.get(self.live_server_url + '/member/login/')
        input_username = self.browser.find_element_by_name('username')
        input_username.send_keys(test_username)

        input_password = self.browser.find_element_by_name('password')
        input_password.send_keys(test_password)

        input_password.send_keys(Keys.ENTER)

        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.current_url, self.live_server_url + '/post/')


class ProfileTest(BaseTestUser):
    def access_profile_page_and_check_status(self, status_name, num):
        self.browser.get(self.make_url('/member/profile/'))
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn(
            '{number} {name}'.format(
                name=status_name, number=num
            ),
            page_text
        )

    def test_pofile_display_status(self):
        user = self.make_user_and_login()
        num = random.randrange(1, 10)
        for i in range(num):
            Post.objects.create(author=user, )
        self.access_profile_page_and_check_status(status_name="posts", num=num)

    def test_profile_display_status_follower_count(self):
        user = self.make_user_and_login()
        ul = make_dummy_users()
        num = random.randrange(1, 10)
        for i in range(num):
            ul[i].follow(user)
        self.access_profile_page_and_check_status(status_name="followers", num=num)

    def test_profile_display_status_following_count(self):
        user = self.make_user_and_login()
        ul = make_dummy_users()
        num = random.randrange(1, 10)
        for i in range(num):
            user.follow(ul[i])
        self.access_profile_page_and_check_status(status_name="following", num=num)
