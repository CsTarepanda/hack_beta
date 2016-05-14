from django.conf.urls import patterns, url
from missphoto import tl, mypage, postUpload, postReaction


urlpatterns = [
    url(r'^$', tl.index, name='index'),
    url(r'^mypage/$', mypage.index, name='mypage'),
    url(r'^upload/$', postUpload.index, name='upload'),
    url(r'^reaction/$', postReaction.index, name='reaction'),
]
