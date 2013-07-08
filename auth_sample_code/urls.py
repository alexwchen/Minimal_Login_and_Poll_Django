from auth_sample_code.views import *
from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', main_page),

    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    # Web portal.
    (r'^portal/', include('portal.urls')),

    # Web portal.
    (r'^polls/', include('polls.urls', namespace="polls")),

    # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
    
    # Admin
    (r'^admin/', include(admin.site.urls)),
)
