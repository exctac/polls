from django.contrib import admin
from django.contrib.admin.widgets import AdminSplitDateTime
from django import forms
from django.core.exceptions import ValidationError

from polls.models import Question, Choice


class QuestionAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionAdminForm, self).__init__(*args, **kwargs)
        self.initial['text'] = ',kfsdsd'

    def clean(self):
        state_old = self.initial.get('state', None)
        state_new = self.cleaned_data.get('state', None)

        if state_new != state_old:
            if state_new == 'a':
                if int(self.data['choice_set-TOTAL_FORMS']) <= 1:
                    self.add_error(None, ValidationError(
                        'Для перехода в состояние Активеный добавьте минимум 2 варианта выбора.',
                        code='invalid'
                    ))
                if state_old != 'n':
                    self.add_error(None, ValidationError(
                        'В состояние Активный можно перейти только из состояния Новый.',
                        code='invalid'
                    ))

            elif state_new == 'f':
                if state_old != 'a':
                    self.add_error(None, ValidationError(
                        'В состояние Завершен можно перейти только из состояния Активный',
                        code='invalid'
                    ))

        return super(QuestionAdminForm, self).clean()

    class Meta:
        model = Question
        fields = ('state', 'question_text', 'pub_date')


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        if obj and obj.state == 'f':
            self.readonly_fields = ('choice_text', 'votes',)
            self.can_delete = False
            self.max_num = False

        if obj and obj.state == 'a':
            self.readonly_fields = ('choice_text',)
            self.can_delete = False
            self.max_num = 0
        a = super(ChoiceInline, self).get_formset(request, obj, **kwargs)
        return a


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline,)
    form = QuestionAdminForm
    list_display = ('question_text', 'state', 'pub_date',)
    list_editable = ('state',)

    def get_form(self, request, obj=None, **kwargs):
        # print(obj.)
        if obj and obj.state == 'f':
            self.readonly_fields = ('state', 'pub_date', 'question_text')
        return super(QuestionAdmin, self).get_form(request, obj, **kwargs)