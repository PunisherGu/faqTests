from django.contrib import admin
from .models import Question
# Register your models here.

#admin.site.register(Question)


class QuestionAdmin(admin.ModelAdmin): #colunas que aparecerao no admin
   list_display = ('text', 'answer', 'ordem')
   
admin.site.register(Question, QuestionAdmin) #registro campo admin
