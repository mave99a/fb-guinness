from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    ('^$', index), 
    ('^index', index), 
    ('^invite', invite),
)
