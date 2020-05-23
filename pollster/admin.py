from django.contrib import admin
from .models import Question,Choice

admin.site.site_header='PollPage'
admin.site.site_title='Covid-19'
admin.site.index_title='Stay Safe'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question_text']}),('date published',{'fields': ['pub_date'] ,'classes':['collapse']}),]
    inlines = [ChoiceInline] #needs to be a list

