from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'bahks.views.index'),
    url(r'^signup$', 'bahks.views.signup'),
    url(r'^storage$', 'bahks.views.boxes'),
    url(r'^login$', 'bahks.views.loginView'),
    url(r'^send$', 'bahks.views.send'),
    url(r'^account$', 'bahks.views.account'),
    url(r'^retrieve/(\d+)$', 'bahks.views.retrieve'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)
