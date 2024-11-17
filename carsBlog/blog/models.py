from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{self.title} | {self.date}'
