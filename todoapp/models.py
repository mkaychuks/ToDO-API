from django.db import models


class Todo(models.Model):
    SEVERITY = [
        ('VERY_IMPORTANT', 'Very Important'),
        ('IMPORTANT', 'Important'),
        ('LESS_IMPORTANT', 'Less Important'),
    ]

    title = models.CharField(max_length=250)
    tag = models.CharField(max_length=21, choices=SEVERITY, default='LESS_IMPORTANT')
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now=True)
    time_created = models.TimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user', null=True, blank=True)


    def __str__(self):
        return f'{self.title} posted by {self.owner.username}'