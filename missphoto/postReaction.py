import django.shortcuts import redirect


def index(request, reaction):
    if request.method == "post":
        return post(request)


def post(request):
    return redirect("reaction")


def get(request):
    return redirect("")
