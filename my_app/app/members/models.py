from django.db import models

# Create your models here.


class Members(models.Model):
    """Create member models"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
