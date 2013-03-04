from django.conf.urls import patterns, include, url

urlpatterns = patterns('rockingsheep.views',
                       url(r'^$', 'index'),
#                       url(r'^$', 'thanks'),
)