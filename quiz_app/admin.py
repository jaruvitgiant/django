from django.contrib import admin
from .models import Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1  # แสดงช่องเพิ่ม choice เพิ่มใน admin

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'published_date')
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'correct')
