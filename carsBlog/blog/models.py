from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'{self.title} | {self.date}'
