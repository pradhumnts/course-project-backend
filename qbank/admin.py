from django.contrib import admin
from .models import *

class TopicAdmin(admin.ModelAdmin):
    list_display = ("topic", "topicAttribute",)

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Answer)
admin.site.register(System)