from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^ghettoping/', hello.views.ghettoping, name='ghettoping'),
    url(r'^submit/', hello.views.submit, name='submit'),
    url(r'^admin/', include(admin.site.urls)),

)
