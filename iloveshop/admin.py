from django.contrib import admin

from .models import ILoveModels, Question

class QuestionAdmin(admin.ModelAdmin):
    fields =['text']

admin.site.register(Question)
admin.site.register(ILoveModels)

# Register your models here.
