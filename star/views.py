from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from models import UpDown

from base64 import b64decode

import StringIO

from PIL import Image


def star_image(offset):
  lock = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA0AAAAyCAMAAACwGaE2AAAAB3RJTUUH1goYBSsdxBNhGAAAACdQTFRF6QGwYWFhubm58fHxwsLC/f393d3dAAAAeHZn//2+/98B+vr6tbW1hi0pPQAAAAF0Uk5TAEDm2GYAAABvSURBVCiRxc3RCsAgCEDRzJpZ+//vnYXmiNgeuw/BScoQfqLeRGXmQoZbRlVJTONuI/IEjbUmL4mrZep/uoqe3yoeLfvOB72JhIgRDJeMkhIQxt1W8Ja9Bh1Zgoxall8Bk2Xq+1xRz29FD5Z9R3sAjzsGHqZ/yuMAAAAASUVORK5CYII=")
  star = b64decode("iVBORw0KGgoAAAANSUhEUgAAABAAAAAwCAMAAAAvgQplAAAAyVBMVEX////8+sz8/vT8jiz8Zhz89vT8ejT86tT8zrz87kT8ukz88nT8/vzs6uz88lz81mz8liT09vT8egz8poT86rz8vpz8+tz87uT89qTc3tz87jT8rjT88mT8+sT8niT8/uz8/tz8jhT89tT8+qzk4uT8Ygz8phz89uz8eiT85sz8zrT87jz8vhz88mz8+vzk5uT87lT89sT8yiT8mhT08vT8bgz8+uz8nlT85sT84lz8spT8+tT8ghT88tT89pzc2tz87iz8shz8VgQWXPWyAAAAAXRSTlMAQObYZgAAATBJREFUKJGVkn1vgjAQh3HzZWhVOidSlJiZwnRoGY6p6JTO7/+hVo6WUaJ/7Gdy5nl63KUEw7gTjGuCUp1ZluktESFR9RwTkhHMAFBEiQglNBM1EhJTReLXgo1goMjBDEA4pob2C9P/W0oh5WKUQy6RukcUYYTyKkWSwBFKkntXv5mGVxOzmc4nl5800eO8V0Hb4y7nng3wMDB5Hjcv5mAu5rtuQeLPbcDAEECocCFHyIdMWw3dFB2bcovsCBXPBXykQu2k8LjpMOSYPJbCucARujj/eh9xXBNpqvNiuz1rYrheDyt4PvyIvBQ9u+40KDPtvhnGKvgsExzynpX1KmOtihGdx2+I1VFD98+Qfbll+QVZKp74vt9uizKR4v3aHDM2bl6fpDiO4GtsjY63rv0LjCMywYpy0lMAAAAASUVORK5CYII=")
  pil = Image.open(StringIO.StringIO(star))
  y = pil.size[1]/3
  yoffset = offset*y
  pil = pil.crop((0,yoffset,pil.size[0],yoffset+y))
  response = HttpResponse(mimetype="image/png")
  pil.save(response, "PNG")
  return response

def star(request):
  """
  number is increased every time the image is displayed/called
  ToDo:
  Do something meaningful with the counter
  """
  if request.session.get('number', False):
    number = request.session['number']
  else:
    request.session['number'] = 0
  
  request.session['number'] += 1
  #result = ""
  #for i in request.META.keys():
  #  result += "%s: %s<br/>"%(i, request.META[i])
  # return HttpResponse(result)
  return star_image(request.session['number']%3)

@require_GET
def script_js(request):
  """
  Assume jQuery is there
  http://alexmarandon.com/articles/web_widget_jquery/

  return js for the widget
  """
  # ToDO
  script = get_template("star/script.js")
  return HttpResponse(script.render())

@require_GET
def style_css(request):
  """
  return the css for the js widget
  """
  # ToDO
  style = get_template("star/style.css")
  return HttpResponse(style.render())


@require_POST
def up(request):
  """
  ajax receiver for the "vote up" button on the widget
  """
  try:
    if request.method == "POST":
      url = request.POST['url']
    else:
      url = request.GET['url']
  except Exception, e:
    return HttpResponse(str(e))

  counter, created = UpDown.objects.get_or_create(absolute_url=url)
  voted = request.session.get(url, False)

  if voted==False or voted=="down":
    counter.up += 1
    counter.save()
    request.session[url] = "up"

  return HttpResponse(str(counter.score()))

@require_POST
def down(request):
  url = request.POST['url']
  counter, created = UpDown.objects.get_or_create(absolute_url=url)
  counter.down += 1
  counter.save()
  return HttpResponse(str(counter.score()))

def score(request):
  if request.method == 'POST':
    url = request.POST['url']
    counter, created = UpDown.objects.get_or_create(absolute_url=url)
    if created:
      counter.save()
    return HttpResponse("%s"%(counter.score))

  if request.method == 'GET':
    if not request.GET.has_key('callback'):
      return HttpResponse("")
    else: # if request.GET['callback']
      cntxt = {
        'url': "123", #request.META['HTTP_REFERER'],
        'token': request.COOKIES['csrftoken'],
      }
      html = "".join(str("""
      <i id="up_%(url)s" class="icon-chevron-up" onclick="$.post('/star/up', {'url':'%(url)s', 'csrfmiddlewaretoken':'%(token)s'}, function(data){ $('#score_%(url)s').html(data); $('#up_%(url)s').addClass('icon-white'); });"></i>
      """%(cntxt)).splitlines())
      jsonp = "%s ( {'html': '%s' } )"
      return HttpResponse(jsonp % (request.GET['callback'], html))
 

