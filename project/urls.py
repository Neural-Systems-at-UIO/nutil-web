from django.conf import settings
from django.contrib import admin
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url
from welcome.views import index, health
from execute import views
#from execute.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    #url('execute/', include(views.index)),
    url('execute/', views.index, name='index'),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
