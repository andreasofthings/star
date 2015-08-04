from django.conf.urls import url, patterns

from django.views.generic import TemplateView
from star.views import Star
urlpatterns = patterns(
    '',
    url(r'^$', Star.as_view(), name='star'),
)
