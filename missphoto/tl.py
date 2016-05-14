import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def index(request):
    return render_to_response('index.html')
