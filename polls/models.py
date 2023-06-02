import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# q =  Question(question_text="question?", pub_date=timezone.now())
# q.save()
# OR
# q = Question.objects.create(question_text="question", pub_date=timezone.now())
# Question.objects.all()
# q = Question.objects.get(pk=1)

# q.choice_set.all()
#   returns all related Choice Models to q
# q.choice_set.create(choice_text="lorem ipsum dolor sit", votes=0)
#   creates a new Choice Model with q relation

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
