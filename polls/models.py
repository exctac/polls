from django.db import models


class Question(models.Model):
    # my code
    CHOISE_NEW = 'n'
    CHOISE_ACTIVE = 'a'
    CHOISE_FINISH = 'f'

    CHOISES = (
        (CHOISE_NEW, 'Новый'),
        (CHOISE_ACTIVE, 'Активный'),
        (CHOISE_FINISH, 'Завершен'),
    )
    state = models.CharField('Status', max_length=255, choices=CHOISES, null=True, blank=True, default=CHOISE_NEW)
    # my code
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # def save(self, *args, **kwargs):
    #     if not self.state:
    #         self.state = 'n'
    #     return super(Question, self).save(*args, **kwargs)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
