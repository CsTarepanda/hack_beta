from django.contrib import admin
# Register your models here.

from .models import Post, Good, Bad, PhotosData, Tag

admin.site.register(Post)
admin.site.register(Good)
admin.site.register(Bad)
admin.site.register(PhotosData)
admin.site.register(Tag)
