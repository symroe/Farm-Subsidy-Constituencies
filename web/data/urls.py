from django.conf.urls.defaults import *

urlpatterns = patterns('data.views',
    url(r'^$','overview', name='overview'),
    url(r'^constituency_list/$','constituency_list', name='constituency_list'),
    url(r'^constituency/(?P<slug>[-\w]+)/$','constituency', name='constituency'),
    url(r'^recipients/$','recipients', name='recipients'),
)