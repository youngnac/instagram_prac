from django.test import TestCase

from member.models import MyUser


def make_user_and_login(client):
    test_username = "test_user"
    test_password = "test_password"
    user = MyUser.objects.create_user(test_username, test_password)
    client.post('/member/login/', {'username': test_username, 'password': test_password})
    return user

class ProfileViewTest(TestCase):
    def test_user_not_authenticated(self):
        url_profile = '/member/profile/'
        response = self.client.get('/member/profile/')
        self.assertRedirects(response, '/member/login/?next={}'.format(url_profile))

    def test_user_authenticated(self):
        # test_username = "test_user"
        # test_password = "test_password"
        # MyUser.objects.create_user(test_username, test_password)
        # self.client.post('/member/login/', {'username': test_username, 'password': test_password})
        make_user_and_login(self.client)
        response = self.client.get('/member/profile/')
        self.assertEqual(response.status_code, 200)


class ChangeProfilePicViewTest(TestCase):
    def test_user_not_authenticated(self):
        url_profile = '/member/profile/photo/'
        response = self.client.get('/member/profile/photo/')
        self.assertRedirects(response, '/member/login/?next={}'.format(url_profile))

    def test_user_authenticated(self):
        make_user_and_login(self.client)
        response = self.client.get('/member/profile/photo/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'member/profile-pic-add.html' )
    #
    # def test_url_resolves_to_profile_img_view(self):
    #     found = resolve('/member/profile/photo/')


class LogoutViewTest(TestCase):
    def test_user_not_authenticated(self):
        url_logout = '/member/logout/'
        response = self.client.get('/member/logout/')
        self.assertRedirects(response, '/member/login/?next={}'.format(url_logout))

    def test_user_authenticated(self):
        make_user_and_login(self.client)
        response = self.client.get('/member/logout/')
        self.assertRedirects(response, '/member/login/')
