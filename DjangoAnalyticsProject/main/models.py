from django.db import models


class Relevance(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='relevance'
    )
    text = models.TextField('Текст', default=None)
    graph_left = models.ImageField(
        'Диаграмма',
        default=None,
        upload_to='relevance'
    )
    table = models.TextField('Таблица', default=None)
    graph_right = models.ImageField(
        'Диаграмма',
        default=None,
        upload_to='relevance'
    )
    table2 = models.TextField('Таблица2', default=None)

    class Meta:
        verbose_name = "Востребованность"
        verbose_name_plural = "Востребованность"

    def __str__(self):
        return self.title


class Geography(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='geography'
    )
    text = models.TextField('Заголовок', default=None)
    graph = models.ImageField(
        'Диаграмма',
        default=None,
        upload_to='geography'
    )
    table = models.TextField('Таблица', default=None)
    graph2 = models.ImageField(
        'Диаграмма',
        default=None,
        upload_to='geography2'
    )
    table2 = models.TextField('Таблица2', default=None)

    class Meta:
        verbose_name = "География"
        verbose_name_plural = "География"

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='skills'
    )
    description = models.TextField('Описание', default=None)
    diagram = models.ImageField('Диаграмма', default=None, upload_to='skills')
    table = models.TextField('Таблица', default=None)

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title
