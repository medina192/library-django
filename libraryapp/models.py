from django.db import models

# Create your models here.
class Author(models.Model):
    name= models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def getAName(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    numberOfPages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def getTitle(self):
        return self.title
    
    def __str__(self):
        return self.title
