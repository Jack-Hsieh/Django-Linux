from django.contrib import admin


# Register your models here.
# 建置後台消息管理系統

from users.models import Post,Pricing,About,Request


admin.site.register(Post)

admin.site.register(Pricing)

admin.site.register(About)

admin.site.register(Request)
