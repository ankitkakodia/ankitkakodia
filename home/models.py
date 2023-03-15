from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    # planning, design, development, testing, or completed
    status = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title