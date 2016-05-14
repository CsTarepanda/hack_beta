import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def login():
    return render_to_response('login.html', ctxt)

def logout():
    return render_to_response('logout.html', ctxt)
