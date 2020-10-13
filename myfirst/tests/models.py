import datetime
from django.db import models
from django.utils import timezone

class Test(models.Model):
    test_title = models.CharField('название статьи', max_length = 200)
    test_text  = models.TextField('текст теста')
    pub_date   = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.test_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class Comment(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    author_name  = models.CharField('имя автора', max_length = 50)
    comment_text = models.TextField('текст коментария', max_length = 200)

    def __str__(self):
        return self.author_name


