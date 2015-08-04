#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
views.py

"""

from django.http import HttpResponse
from django.views import View
from base64 import b64decode

import StringIO

from PIL import Image


class Star(View):
    star = b64decode("iVBORw0KGgoAAAANSUhEUgAAABAAAAAwCAMAAAAvgQplAAAAyVBMVEX////8+sz8/vT8jiz8Zhz89vT8ejT86tT8zrz87kT8ukz88nT8/vzs6uz88lz81mz8liT09vT8egz8poT86rz8vpz8+tz87uT89qTc3tz87jT8rjT88mT8+sT8niT8/uz8/tz8jhT89tT8+qzk4uT8Ygz8phz89uz8eiT85sz8zrT87jz8vhz88mz8+vzk5uT87lT89sT8yiT8mhT08vT8bgz8+uz8nlT85sT84lz8spT8+tT8ghT88tT89pzc2tz87iz8shz8VgQWXPWyAAAAAXRSTlMAQObYZgAAATBJREFUKJGVkn1vgjAQh3HzZWhVOidSlJiZwnRoGY6p6JTO7/+hVo6WUaJ/7Gdy5nl63KUEw7gTjGuCUp1ZluktESFR9RwTkhHMAFBEiQglNBM1EhJTReLXgo1goMjBDEA4pob2C9P/W0oh5WKUQy6RukcUYYTyKkWSwBFKkntXv5mGVxOzmc4nl5800eO8V0Hb4y7nng3wMDB5Hjcv5mAu5rtuQeLPbcDAEECocCFHyIdMWw3dFB2bcovsCBXPBXykQu2k8LjpMOSYPJbCucARujj/eh9xXBNpqvNiuz1rYrheDyt4PvyIvBQ9u+40KDPtvhnGKvgsExzynpX1KmOtihGdx2+I1VFD98+Qfbll+QVZKp74vt9uizKR4v3aHDM2bl6fpDiO4GtsjY63rv0LjCMywYpy0lMAAAAASUVORK5CYII=")

    def get(self, request):
        pil = Image.open(StringIO.StringIO(self.star))
        response = HttpResponse(mimetype="image/png")
        pil.save(response, "PNG")
        return response


def star_image(offset):
    # lock = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA0AAAAyCAMAAACwGaE2AAAAB3RJTUUH1goYBSsdxBNhGAAAACdQTFRF6QGwYWFhubm58fHxwsLC/f393d3dAAAAeHZn//2+/98B+vr6tbW1hi0pPQAAAAF0Uk5TAEDm2GYAAABvSURBVCiRxc3RCsAgCEDRzJpZ+//vnYXmiNgeuw/BScoQfqLeRGXmQoZbRlVJTONuI/IEjbUmL4mrZep/uoqe3yoeLfvOB72JhIgRDJeMkhIQxt1W8Ja9Bh1Zgoxall8Bk2Xq+1xRz29FD5Z9R3sAjzsGHqZ/yuMAAAAASUVORK5CYII=")
    pass
