import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def index(request):
    #response = json.dumps({'tags_id': tags_id})
    #return HttpResponse(response, content_type="application/json")
    return render_to_response('mypage.html')
