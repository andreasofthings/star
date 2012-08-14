from django.conf import settings
from django.conf.urls.defaults import *

import views

urlpatterns = patterns('star.views',
  url(r'^$', 'star', name='tracking_star'),
  url(r'^/script.js$', 'script_js', name='tracking_js'),
  url(r'^/style.css$', 'style_css', name='tracking_css'),
  url(r'^/up$', 'up', name='tracking_up'),
  url(r'^/down$', 'down', name='tracking_down'),
)

urlpatterns += patterns('star.views',
  url(r'^/score$', 'score', name='tracking_score'),
)
