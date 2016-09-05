from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('redis_test.urls')),
    url(r'^accounts/login', 'django.contrib.auth.views.login',
        name='login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    url(r'^accounts/logout',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={
            'next_page': '/'
        }
    ),
]
