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
    graph_right = models.ImageField(
        'График №1',
        default=None,
        upload_to='relevance'
    )


class Geography(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='geography'
    )
    text = models.TextField('Заголовок', default=None)
    table = models.TextField('Таблица', default=None)
    graph = models.ImageField(
        'График',
        default=None,
        upload_to='geography'
    )


class Skills(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='skills'
    )
    graph_2015 = models.ImageField('График 2015',default=None,upload_to='skills2015')
    graph_2016 = models.ImageField('График 2016',default=None,upload_to='skills2016')
    graph_2017 = models.ImageField('График 2017',default=None,upload_to='skills2017')
    graph_2018 = models.ImageField('График 2018',default=None,upload_to='skills2018')
    graph_2019 = models.ImageField('График 2019',default=None,upload_to='skills2019')
    graph_2020 = models.ImageField('График 2020',default=None,upload_to='skills2020')
    graph_2021 = models.ImageField('График 2021',default=None,upload_to='skills2021')
    graph_2022 = models.ImageField('График 2022',default=None,upload_to='skills2022')
    graph_2023 = models.ImageField('График 2023',default=None,upload_to='skills2023')
    graph_2024 = models.ImageField('График 2024',default=None,upload_to='skills2024')
    text = models.TextField('Текст', default=None)
