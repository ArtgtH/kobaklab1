"""Здесь находится класс, который будет осуществлять передачу данных"""
from django.shortcuts import render

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Data
from .serializers import DataSerializer


class DataApiView(ModelViewSet):
    """

    View-класс для передачи данных.
    В нем осуществлена сортировка данных по по полям:
        'axis_X',
        'axis_Y',
        'rotation',
        'font_size',
        'font_type',
        'data_type',
        'batch',

    Также сделан поиск по партиям данных (поле batch)
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = [
        OrderingFilter,
        SearchFilter,
    ]
    search_fields = [
        'batch',
    ]
    ordering_fields = [
        'axis_X',
        'axis_Y',
        'rotation',
        'font_size',
        'font_type',
        'data_type',
        'batch',
    ]
