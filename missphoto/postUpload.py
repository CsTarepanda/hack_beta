from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from missphoto.models import *
from time import time

import json
import subprocess


def index(request):
    if request.method == "POST":
        return post(request)
    else:
        return get(request)


def post(request):
    for name, value in request.FILES.items():
        filename = "missphoto/static/photos/{}{}.{}".format(request.user, int(time()), str(value).split(".")[-1])
        default_storage.save(filename, ContentFile(value.read()))
        post = Post(user_id=request.user)
        post.save()
        # - - - 無理やり cloud vision
        subprocess.call("php missphoto/gcv.php {} > missphoto/gcv_result".format(filename), shell=True)
        re = open("missphoto/gcv_result")
        re.readline()
        result = "{"
        for i in re:
            if i.startswith("<"):
                break
            result += i

        result = json.loads(result)
        result = result.get("responses")[0].get("labelAnnotations")
        result = [x.get("description") for x in result]
        # - - -
        print(result)
        for i in result:
            Tag(post_id=post, name=i).save()
        PhotosData(post_id=post, name="Gorilla").save()
    return redirect(reverse("upload"))


def get(request):
    return redirect(reverse("index"))
