import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def index(request):
    response = json.dumps({'id': 12})
    ctxt = RequestContext(request, {'data': response})
    return render_to_response('index.html', ctxt)
