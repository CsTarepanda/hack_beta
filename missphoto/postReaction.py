from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from missphoto.models import Good, Bad, Post


def index(request, reaction):
    if request.method == "POST":
        if reaction == "good":
            return good_post(request, request.POST)
        elif reaction == "bad":
            return bad_post(request, request.POST)
        else:
            return get(request)


def good_post(request, post_data):
    post_id = post_data.get("post_id")
    good = Good.objects.filter(user_id=request.user).filter(post_id=post_id)
    if good.exists():
        good[0].delete()
        return redirect(reverse("index"))
    post = Post.objects.get(id=post_id)
    Good(user_id=request.user, post_id=post).save()
    return redirect(reverse("upload"))


def bad_post(request, post_data):
    post_id = post_data.get("post_id")
    bad = Bad.objects.filter(user_id=request.user).filter(post_id=post_id)
    if bad.exists():
        bad[0].delete()
        return redirect(reverse("index"))
    post = Post.objects.get(id=post_id)
    Bad(user_id=request.user, post_id=post).save()
    return redirect(reverse("upload"))


def get(request):
    return redirect(reverse("index"))
