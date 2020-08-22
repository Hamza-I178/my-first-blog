from django.contrib import admin
from .models import Post, CV, Public_CV

admin.site.register(Post)
admin.site.register(CV)
admin.site.register(Public_CV)