import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from missphoto.models import *

def index(request):
    tl = Post.objects.all()
    return render_to_response('index.html',
            RequestContext(request, { 'tl': tl }))
