from django.contrib import admin

# Register your models here.
from django.contrib import admin
from publish.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


