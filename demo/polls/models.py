# -*- coding_ utf-8 -*-

from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

    class Meta:
        drf_config = {
            'api': {
                'scaffolding': True,
                'methods': ['CREATE', 'UPDATE']
            },
            'serializer': {
                'fields': [
                    'title'
                ]
            }
        }


class Question(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll, related_name='questions')

    class Meta:
        drf_config = {
            'api': {
                'scaffolding': True,
                'methods': ['CREATE', 'UPDATE']
            },
            'serializer': {
                'scaffolding': True
            }
        }
