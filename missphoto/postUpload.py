from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from time import time


def index(request):
    if request.method == "POST":
        return post(request)
    else:
        return get(request)


def post(request):
    for name, value in request.FILES.items():
        default_storage.save("missphoto/static/photos/{}{}.{}".format(request.user, int(time()), str(value).split(".")[-1]), ContentFile(value.read()))
    return redirect(reverse("upload"))


def get(request):
    return redirect(reverse("index"))
