from django.shortcuts import redirect


def index(request):
    if request.method == "post":
        return post(request)
    else:
        return get(request)


def post(request):
    for i in request.FILES:
        print(i)
    return redirect("upload")


def get(request):
    return redirect("")
