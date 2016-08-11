from django.contrib import admin

# Register your models here.
from .models import *

# Class to add choices "inline"
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Custom class, to be be passed as second arg
# When you want to change the admin site for a model
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)