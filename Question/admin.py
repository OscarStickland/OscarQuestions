from django.contrib import admin
from .models import Question, Answer, AdminUser


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'answer_date')

# Register your models here.
admin.site.register(Question)
admin.site.register(AdminUser)
admin.site.register(Answer, AnswerAdmin)
