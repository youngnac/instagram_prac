from django.conf.urls import url

from . import views

app_name = 'member'
urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_modelform_view, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/photo/$', views.change_profile_image, name='profile-pic-add'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
