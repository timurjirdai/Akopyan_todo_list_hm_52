from django.db import models


class Task(models.Model):

    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано'),
    ]

    description = models.TextField()

    details = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.description