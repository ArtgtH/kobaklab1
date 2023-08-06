"""Тут находятся модели для БД."""
from django.db import models


class Data(models.Model):
    """Модель данных для загрузки в БД."""

    text = models.CharField(default='foo', max_length=100)
    axis_X = models.IntegerField(default=0)
    axis_Y = models.IntegerField(default=0)
    rotation = models.IntegerField(default=0)
    font_size = models.IntegerField(default=0)
    font_type = models.CharField(default='foo', max_length=100)
    data_type = models.CharField(default='foo', max_length=100)
    batch = models.IntegerField(default=0)
