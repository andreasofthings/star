from django.conf import settings
from django.conf.urls.defaults import *

import views

urlpatterns = patterns('star.views',
  url(r'^$', 'star', name='tracking_star'),
  url(r'^/static/script.js$', 'script_js', name='tracking_js'),
  url(r'^/static/style.css$', 'style_css', name='tracking_css'),
  url(r'^/vote/up$', 'up', name='tracking_up'),
  url(r'^/vote/down$', 'down', name='tracking_down'),
)

urlpatterns += patterns('star.views',
  url(r'^/score$', 'score', name='tracking_score'),
)

from django.views.generic import TemplateView

urlpatterns += patterns('star.views',
  # include this
  url(r'^/star.js$', TemplateView.as_view(template_name="star/star.js"), name="star_js"),
  # receives data 
  url(r'^/star$', 'star_callback', name='star_callback'),
  # style
  url(r'^/static/star.css$', TemplateView.as_view(template_name="star/star.css"), name='star_css'),
  
  # demo.html
  url(r'^/demo.html$', TemplateView.as_view(template_name="star/demo.html"), name='star_demo'),
)
