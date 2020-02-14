from django.db import models


class Author(models.Model):
    name = models.CharField('AuthorName', unique=True, max_length=32)
    age =  models.SmallIntegerField('AuthorAge', default=0)
    desc = models.TextField('AuthorAge', default=0)
    created = models.DateTimeField('Created Time', auto_now_add=True)
    updated = models.DateTimeField('Updated Time', auto_now=True)

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return (f'{self.name}')


class Book(models.Model):
    TYPE_CHOICE = {
        (0, '英语书'),
        (1, '小黄书')
    }
    title = models.CharField('BookTitle', unique=True, max_length=32)
    author = models.ManyToManyField(to=Author)
    url = models.CharField('BookUrl', max_length=256, blank=True, default='')
    ctype = models.SmallIntegerField('BookType', choices=TYPE_CHOICE, default=0)
    created = models.DateTimeField('Created Time', auto_now_add=True)
    updated = models.DateTimeField('Updated Time', auto_now=True)

    class Meta:
        db_table = 'book'
        verbose_name = '书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return (f'{self.title}')

