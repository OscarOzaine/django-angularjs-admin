from retail.views import User
#ChainViewSet, StoreViewSet, EmployeeViewSet, User
from django.conf.urls import url
from retail import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers, serializers, viewsets
from django.conf.urls import include

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(prefix='chains', viewset=ChainViewSet)
#router.register(prefix='stores', viewset=StoreViewSet)
#router.register(prefix='employees', viewset=EmployeeViewSet)
#router.register(prefix='users/login', viewset=User)
#router.register(prefix='example', viewset=ExampleView)

#router.register(prefix='api-auth/', viewset=User)
urlpatterns = [
	url(r'^snippets/$', views.SnippetList.as_view()),
	#url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns = [
# 	url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
# 	#url(r'/users/$', views.User.as_view({'get': 'list'})),
# 	#url(r'/users/(?P<pk>[0-9]+)/$', views.User.as_view({'get': 'list'}))
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
#urlpatterns += router.urls
