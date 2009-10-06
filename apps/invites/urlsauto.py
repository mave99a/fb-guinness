from django.conf.urls.defaults import *

rootpatterns = patterns('',
    (r'', include('invites.urls')),
)