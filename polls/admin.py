from django.contrib import admin

from django.contrib import admin

from .models import Question, Choice



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'nombre', 'apellido', 'comentario')
    fields = ['question_text','pub_date','nombre','apellido','comentario']
    #list_filter = ['question_text','nombre','apellido']
    search_fields = ['question_text','nombre','apellido','comentario']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
