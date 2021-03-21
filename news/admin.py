from django.contrib import admin

# Register your models here.
from news.models import Posts, Comments

admin.site.register(Posts, Comments)
