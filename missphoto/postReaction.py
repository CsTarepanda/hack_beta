from django.shortcuts import redirect


def index(request, reaction):
    if request.method == "post":
        if reaction == "fav":
            return good_post(request)
        elif reaction == "bad":
            return bad_post(request)


def good_post(request):
    return redirect("reaction")


def bad_post(request):
    return redirect("reaction")


def get(request):
    return redirect("")
