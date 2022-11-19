from django.contrib import admin
from .models import *
admin.site.site_header = 'DidEduComp admin'

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Comment)