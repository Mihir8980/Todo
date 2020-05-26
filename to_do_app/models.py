from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=200)
    added_date = models.DateTimeField()
    flag = models.BooleanField(default=False)    

    def __str__(self):
        return "Text: " + self.text + "  Time: " + self.added_date.strftime("%m/%d/%Y, %H:%M:%S")