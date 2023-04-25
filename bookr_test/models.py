from django.db import models

# Create your models here.

class Publisher(models.Model):
    """ A Company that publishes books. """
    name = models.CharField(max_length=50, help_text="The name of the publisher.")
    website = models.URLField(help_text="The Publisher's website")
    email = models.EmailField(help_text="The Publisher's email address ")
    
    def __str__(self):
        return self.name