from django.contrib import admin
from .models import Category,Answer,Questions,Comment
# Register your models here.
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Category)

