from django.db import models


class Relevance(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='relevance'
    )
    text = models.TextField('Текст', default=None)
    graph_left = models.ImageField(
        'График №2',
        default=None,
        upload_to='relevance'
    )
    table = models.TextField('Таблица', default=None)
    graph_right = models.ImageField(
        'График №1',
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
        'График',
        default=None,
        upload_to='geography'
    )
    table = models.TextField('Таблица', default=None)
    graph2 = models.ImageField(
        'График2',
        default=None,
        upload_to='geography2'
    )
    table2 = models.TextField('Таблица2', default=None)

    class Meta:
        verbose_name = "География"
        verbose_name_plural = "География"

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='skills'
    )
    text = models.TextField('Текст', default=None)
    graph_2015 = models.ImageField('График 2015', default=None, upload_to='skills2015')
    table = models.TextField('Таблица', default=None)
    graph_2016 = models.ImageField('График 2016', default=None, upload_to='skills2016')
    table2 = models.TextField('Таблица', default=None)
    graph_2017 = models.ImageField('График 2017', default=None, upload_to='skills2017')
    table3 = models.TextField('Таблица', default=None)
    graph_2018 = models.ImageField('График 2018', default=None, upload_to='skills2018')
    table4 = models.TextField('Таблица', default=None)
    graph_2019 = models.ImageField('График 2019', default=None, upload_to='skills2019')
    table5 = models.TextField('Таблица', default=None)
    graph_2020 = models.ImageField('График 2020', default=None, upload_to='skills2020')
    table6 = models.TextField('Таблица', default=None)
    graph_2021 = models.ImageField('График 2021', default=None, upload_to='skills2021')
    table7 = models.TextField('Таблица', default=None)
    graph_2022 = models.ImageField('График 2022', default=None, upload_to='skills2022')
    table8 = models.TextField('Таблица', default=None)
    graph_2023 = models.ImageField('График 2023', default=None, upload_to='skills2023')
    table9 = models.TextField('Таблица', default=None)
    graph_2024 = models.ImageField('График 2024', default=None, upload_to='skills2024')
    table10 = models.TextField('Таблица', default=None)

    class Meta:
        verbose_name = "Навыки"
        verbose_name_plural = "Навыки"

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
        verbose_name_plural = "Навык"

    def __str__(self):
        return self.title
