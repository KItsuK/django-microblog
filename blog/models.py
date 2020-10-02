from django.db import models

class Blog(models.Model):
    content = models.CharField(max_length=140, verbose_name='本文') #投稿内容
    posted_date = models.DateTimeField(auto_now_add=True) #投稿日時

    class Meta:
        ordering = ['-posted_date']
