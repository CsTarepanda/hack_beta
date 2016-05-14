from django.shortcuts import redirect


def index(request):
    pass
    if request.method == "post":
        return post(request)
    else:
        return get(request)


def post(request):
    return redirect("upload")


def get(request):
    return redirect("")
