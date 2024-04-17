from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=250)
    home_number = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class News(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='news/%Y/%m/%d', blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name