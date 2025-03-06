from django.db import models

# Create your models here.
class Task(models.Model):
    status_choices = [('pending', 'Čeká na splnění.'), ('done', 'Hotovo.'),]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return self.title