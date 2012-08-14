from django import template
from django.core.urlresolvers import reverse
from .. import models

register = template.Library()

class StarNode(template.Node):
  """<a href="https://twitter.com/share" class="twitter-share-button" data-via="deltabps" data-lang="de">Twittern</a>
  <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>"""
  def __init__(self):
  	pass
  def render(self, context):
    return """<img src="%s"/>"""%(reverse('star-png'))

@register.tag
def star(parser, token):
  return StarNode()

class UpDownNode(template.Node):
  def __init__(self, absolute_url):
    self.absolute_url = template.Variable(absolute_url)
  def render(self, context):
    try:
      actual_url = self.absolute_url.resolve(context)
    except template.VariableDoesNotExist:
      return "NoSuchVariable"

    try:
      updown, created = models.UpDown.objects.get_or_create(absolute_url=actual_url)
    except:
      return "countefuckup"
      
    if created:
      updown.save()

    up_clicked = """<i class="icon-chevron-up icon-white\"></i>"""
    down_clicked = """<i class="icon-chevron-down icon-white"></i>"""

    jscntxt = {
      'url': actual_url,
      'token': context['csrf_token'],
      'upclick': up_clicked,
    }

    request = context['request']
    voted = request.session.get(actual_url, False)


    if voted == "up":
      up = up_clicked
    else:
      up = """
        <i id="up_%(url)s" class="icon-chevron-up" onclick="$.post('/star/up', {'url':'%(url)s', 'csrfmiddlewaretoken':'%(token)s'}, function(data){ $('#score_%(url)s').html(data); $('#up_%(url)s').addClass('icon-white'); });"></i>
      """%(jscntxt)

    if voted == "down":
      down = down_clicked
    else:
      down = """
        <i id="down_%(url)s" class="icon-chevron-down" onclick="$.post('/star/down', {'url':'%(url)s', 'csrfmiddlewaretoken':'%(token)s'}, function(data){ $('#score_%(url)s').html(data); $('#down_%(url)s').addClass('icon-white'); });"></i>
      """%(jscntxt)

    return """%s <div id="score_%s">%s</div> %s""" %( up,  updown.absolute_url, updown.score(), down)

@register.tag
def updown(parser, token):
  try:
    tag_name, absolute_url = token.split_contents()
  except ValueError:
    raise template.TemplateSyntaxError("%r requires an absolute object URL as a single argument"% token.contents.split()[0])
  return UpDownNode(absolute_url)
