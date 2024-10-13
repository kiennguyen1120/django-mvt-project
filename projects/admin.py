from django.contrib import admin

# Register your models here.
# đăng ký model với Django admin để model đó có thể được quản lý qua giao diện quản trị của Django.
from .models import Project,Review,Tag

# telling Django, get this model and show it in the admin panel
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)

