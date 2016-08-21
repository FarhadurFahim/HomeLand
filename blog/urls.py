from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^HomeLand/$', views.home_land, name='home_land'),
    url(r'^logout/$', views.user_logout, name='logout'),
    
    url(r'^profile/(?P<pk>\d+)/$',
        views.UserProfileDetail.as_view(),
        name='user_profile_detail'),
   # url(r'^(?P<pk>\d+)/update/$',views.UserProfileUpdate, name='UserProfileUpdate'),



    url(r'^profile/(?P<pk>\d+)/update/$',views.UserProfileUpdate.as_view(success_url="/profile/("), name='user_profile_edit'),


]
