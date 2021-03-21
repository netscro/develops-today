from django.contrib import admin

# Register your models here.
from news.models import Comments, Posts

admin.site.register(Posts)
admin.site.register(Comments)
