from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        return redirect(reverse("missphoto:index"))
        # else:
        #     return redirect("missphoto:index")
    else:
        return redirect("/login/")
        # Return an 'invalid login' error message.
