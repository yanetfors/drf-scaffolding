# -*- coding_ utf-8 -*-

from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

    class Meta:
        drf_config = {
            'api': True
        }


class Question(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

    class Meta:
        drf_config = {
            'api': True,
            'fields': [
                'title'
            ]
        }
