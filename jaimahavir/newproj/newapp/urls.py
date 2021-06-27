from django.conf.urls import url
from newapp import views
from django.conf import settings

app_name='newapp'
urlpatterns = [
     url(r'^register/$', views.register, name='register'),
      url(r'^index/$', views.index, name='index'),
      url(r'^user_login/$', views.user_login, name='user_login'),
      url(r'^member_detail/$', views.member_detail, name='member_detail'),
      url(r'^update/(?P<pk>\d+)//$',views.MemberUpadteView.as_view(),name='update'),
      url(r'^donate/$', views.donate, name='donate'),


]
