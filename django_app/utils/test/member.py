from member.models import MyUser


__all__ = (
    'make_dummy_users',

)


def make_dummy_users():
    ul = []
    for i in range(10):
        username = "testuser{}".format(i + 1)
        password = "dudsk123"
        ul.append(MyUser.objects.create(
            username=username,
            password=password
        ))
    return ul
