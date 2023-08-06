"""Здесь будет находится сериализатор, который отвечает за формат передачи данных."""

from rest_framework import serializers

from .models import Data

class DataSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для модели Data"""
    class Meta:
        model = Data
        fields = (
            'text',
            'axis_X',
            'axis_Y',
            'rotation',
            'font_size',
            'font_type',
            'data_type',
            'batch',
        )
