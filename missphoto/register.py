from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

def index(request):
    if request.GET.get("page"):
        return render_to_response("register.html", RequestContext(request, {
            }))

    if request.method == "POST":
        user = User.objects.create_user(username=request.POST.get("username"), password=request.POST.get("password"))
        print(user)
        return redirect(reverse("register"))
    return redirect(reverse("login"))
