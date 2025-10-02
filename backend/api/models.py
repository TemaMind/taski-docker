"""Модели."""

from django.db import models


class Task(models.Model):
    """Модель-задача."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
