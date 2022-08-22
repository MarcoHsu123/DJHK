"""
Definition of urls for hike.
"""

from django.conf.urls import include, url
from events import views
from django.conf import settings
from django.conf.urls.static import serve ,static


from events.views import article , detail


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    

    # Examples:
    #url(r'^$', hike.views.home, name='home'),
    url(r'^hike/$',views.hike ),
    url(r'^hike/(?P<page>\d{1,3})/',views.hike ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', django.contrib.admindocs.urls),

    # Uncomment the next line to enable the admin:
    url(r'^admin/',admin.site.urls),
    
    #url(r'',admin.site.urls),

    #events url
    url(r'$',article,name = 'article'),
    url(r'^events/$',article,name = 'article'),
    url(r'^events/(?P<page>\d{1,3})/',article,name = 'article'),

    url(r'^events/detail/(?P<eid>\d{1,3})/$',detail,name = 'detail')
    
    #url(r'<int:id>/<int:page>.html',article,name = 'article'),
    
]

