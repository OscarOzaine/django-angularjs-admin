from internal.views import User
#ChainViewSet, StoreViewSet, EmployeeViewSet, User
from internal import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
	url(r'^range-parameter/$', views.RangeParameterList.as_view()),
	url(r'^login/$', views.AuthLogin.as_view()),
	url(r'^api-token-auth/', obtain_jwt_token),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
