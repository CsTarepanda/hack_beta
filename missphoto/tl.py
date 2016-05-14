import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from missphoto.models import *
from django.core import serializers

def index(request):
    tl = Post.objects.all()
    # for i in tl:
    #     i.tag = i.tag_set.all()
    return render_to_response('index.html',
            RequestContext(request, { 'tl': tl }))
