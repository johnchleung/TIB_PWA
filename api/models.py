import datetime

from django.db import models
from django.utils import timezone
from django.db.models import Func

# Testing items
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
# End of testing items


# Pre-defined tables
class Left(Func):
    function = 'LEFT'
    template = '%(function)s(%(expressions)s, 256)'

class Tbltib(models.Model):
    fldID = models.AutoField(primary_key=True) # length=11
    fldNo = models.CharField(max_length=50, db_index=True)
    fldStatus = models.CharField(max_length=20)
    fldCoordinate = models.CharField(max_length=200)
    fldOrientation = models.CharField(max_length=20)
    fldPicture = models.TextField(null=True, blank=True)  # Allowing null values
    fldLastMDate = models.DateTimeField(default="0001-01-01 00:00:00")
    fldEmpNameM = models.CharField(max_length=250)

    class Meta:
        db_table = 'Tbltib'
        managed = False

    def __str__(self):
        return self.fldNo

    @property
    def fldPicture_short(self):
        return Tbltib.objects.annotate(fldPicture_short=Left('fldPicture')).get(pk=self.pk).fldPicture_short