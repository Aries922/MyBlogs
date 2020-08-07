from django.db import models

# Create your models here.
class Feed(models.Model):
    sno=models.AutoField(primary_key= True)
    heading=models.CharField( max_length=50)
    author=models.CharField( max_length=50)
    content=models.TextField()
    slug = models.SlugField(max_length=140, unique=True)
    date=models.DateTimeField( blank=True)
    

    def __str__(self):
        return self.heading+' by ' +self.author 
    