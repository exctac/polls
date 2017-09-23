from django.db import models


class Question(models.Model):
    CHOICE_NEW = 1
    CHOICE_ACTIVE = 2
    CHOICE_FINISH = 3

    CHOICES = (
        (CHOICE_NEW, 'Новый'),
        (CHOICE_ACTIVE, 'Активный'),
        (CHOICE_FINISH, 'Завершен'),
    )
    state = models.IntegerField('Status', choices=CHOICES, default=CHOICE_NEW, blank=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def is_new(self):
        return self.state == self.CHOICE_NEW

    def is_active(self):
        return self.state == self.CHOICE_ACTIVE

    def is_finish(self):
        return self.state == self.CHOICE_FINISH

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
