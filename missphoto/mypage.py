import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from missphoto.models import *


def index(request):
    #response = json.dumps({'tags_id': tags_id})
    #return HttpResponse(response, content_type="application/json")
    posts = Post.objects.filter(user_id=request.user)
    for i in posts:
        i.score = Good.objects.filter(post_id=i).count() - Bad.objects.filter(post_id=i).count()
    model = sorted(posts, key=lambda x: x.score)
    return render_to_response('mypage.html', RequestContext(request, {
        "models": model
        }))
