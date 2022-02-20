import imp
from django.contrib import admin
from . import models


class PostAdminModel(admin.ModelAdmin):
    list_display = ("name","published")


admin.site.register(models.Post,PostAdminModel)
