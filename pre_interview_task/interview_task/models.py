from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    description = models.TextField()
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Tile(models.Model):
    launch_date = models.DateField()
    status_choices = (
        ('live', 'Live'),
        ('pending', 'Pending'),
        ('archived', 'Archived')
    )
    status = models.CharField(max_length=10, choices=status_choices)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return f'Tile {self.id}'
