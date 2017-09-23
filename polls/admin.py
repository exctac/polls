from django.contrib import admin
from django.contrib.admin.widgets import AdminSplitDateTime
from django import forms
from django.core.exceptions import ValidationError

from polls.models import Question, Choice


class QuestionAdminForm(forms.ModelForm):

    def clean_state(self):
        state_initial = self.initial.get('state', None)
        state_cleaned = self.cleaned_data.get('state', None)
        difference = state_cleaned - state_initial

        if difference:
            if difference < 0:
                raise ValidationError(
                    'Переход к предыдущему статусу НЕ возможен, следующий допустимый статус "Завершен"',
                    code='invalid'
                )
            elif difference > 1:
                raise ValidationError(
                    'В статус "Завершен" можно перейти только из состояния "Активный"',
                    code='invalid'
                )

        return state_cleaned

    class Meta:
        model = Question
        fields = ('state', 'question_text', 'pub_date')
        help_texts = {
            'state': ('Вы сможете поменять статус Вопроса, после создания и '
                      'сохранения как мимнимум 2-х вариантов ответов!'),
        }


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ('choice_text', 'votes',)
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        if obj:
            if obj.is_active() or obj.is_finish():
                self.can_delete = False
                self.max_num = 0
                self.readonly_fields = ('choice_text',) if obj.is_active() else ('choice_text', 'votes',)
        return super(ChoiceInline, self).get_formset(request, obj, **kwargs)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline,)
    form = QuestionAdminForm
    list_display = ('question_text', 'state', 'pub_date',)
    fields = ('state', 'pub_date', 'question_text')
    readonly_fields = ('state',)

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.choice_set.count() >= 2:
            return () if not obj.is_finish() else ('state', 'pub_date', 'question_text',)
        return self.readonly_fields
