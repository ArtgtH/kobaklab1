from django.contrib import admin
from django.urls import path, include

from .views import DataApiView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('data_model', DataApiView)


urlpatterns = [
    path('api/', include(router.urls)),
]
