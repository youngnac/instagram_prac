from django.conf.urls import url

from . import views

app_name = 'post'
urlpatterns = [
    url(r'^$', views.post_list, name='post-list'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='post-detail',),
    url(r'^(?P<post_id>[0-9]+)/comment/add/$', views.comment_add, name='comment_add',),

]
