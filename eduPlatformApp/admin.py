from django.contrib import admin
from .models import *
admin.site.site_header = "DidEduComp Admin"
admin.site.site_title = "DidEduComp Admin"
admin.site.index_title = "DidEduComp Admin"
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Comment)