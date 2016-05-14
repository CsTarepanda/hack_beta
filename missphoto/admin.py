from django.contrib import admin
# Register your models here.

from .models import Posts
from .models import Posts, Goods, Bads, Photos_datas

admin.site.register(Posts)
admin.site.register(Goods)
admin.site.register(Bads)
admin.site.register(Photos_datas)
