from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def index(request):
    if request.method == "POST":
        return post(request)
    else:
        return get(request)


def post(request):
    for name, value in request.FILES.items():
        default_storage.save("missphoto/static/photos/{}".format(value), ContentFile(value.read()))
    return redirect(reverse("upload"))


def get(request):
    return redirect(reverse("index"))
