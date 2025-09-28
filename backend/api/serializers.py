"""Сериализер."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор задачи."""

    class Meta:
        """Поля."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
