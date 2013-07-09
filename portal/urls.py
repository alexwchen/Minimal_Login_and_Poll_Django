from django.conf.urls.defaults import *
from portal.views import *

urlpatterns = patterns('',

    # Main web portal entrance.
    (r'^$', portal_main_page),
    (r'^test$', user_test),
    (r'^contact$', contact),
    (r'^register$', register),


)
