from django.conf.urls.defaults import url, patterns

from django.views.generic import TemplateView

urlpatterns = patterns(
    'star.views',
    url(r'^$', 'count', name='star'),
    url(r'^/score$', 'count_score', name='count_score'),
    url(r'^/vote/up$', 'count_up', name='count_up'),
    url(r'^/vote/down$', 'count_down', name='count_down'),
    url(
        r'^/static/count.js$',
        TemplateView.as_view(template_name='count.js'),
        name='count_js'
    ),
    url(
        r'^/static/count.css$',
        TemplateView.as_view(template_name='count.css'),
        name='count_css'
    ),
)


urlpatterns += patterns(
    'star.views',
    # include this
    url(
        r'^/star.js$',
        TemplateView.as_view(template_name="star/star.js"),
        name="js"
    ),
    # receives data
    url(r'^/star$', 'star_callback', name='star_callback'),
    # style
    url(
        r'^/static/star.css$',
        TemplateView.as_view(template_name="star/star.css"),
        name='css'
    ),

    # demo.html
    url(
        r'^/demo.html$',
        TemplateView.as_view(template_name="star/demo.html"),
        name='demo'
    ),
)
