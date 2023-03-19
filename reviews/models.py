from django.db import models

# Create your models here.


class Publisher(models.Model):
    """ A company that publishes books. """
    name = models.CharField(max_length=50,help_text="The name of the Publisher.")
    website = models.URLField(help_text="The Publisher website")
    email = models.EmailField()
    

class Book(models.Model):
    """ A published book. """ 
    title = models.CharField(max_length=70,help_text="The title of the book")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isb = model.charField(max_length=20,verbose_name="ISBN number of the book")
    publisher = models.ForeignKey(Publisehr, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor',through="BookContributor")
    

class Contributor(models.Model):
    """ A contributor to a Book , e.g author, editor, co-author. """ 
    first_names = models.CharField(max_length=50,help_text="The contributor's first name or name")
    last_names =models.CharField(max_length=50,help_text="The contributor's last name or names")
    email = models.EmailField(help_text="The contact email for the contributor.")

class BookContributors(models)
