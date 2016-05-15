from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, views

def login(request):
    if request.method != "POST":
        return render_to_response("login.html", RequestContext(request, {
            }))
    print("okokokok")
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        if not username:
            user = User.objects.create_user(
                    username=username,
                    password=password,
                    )
        print("ok")
        print(user)
        user = user[0]
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
    except:
        return redirect("/login/")

def logout(request):
    views.logout(request)
    return redirect("/login")
