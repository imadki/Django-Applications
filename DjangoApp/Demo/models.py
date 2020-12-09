from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Voie(models.Model):
    
    region =       models.ForeignKey(Region,   on_delete=models.SET_NULL, null=True)
    city =         models.ForeignKey(City,      on_delete=models.SET_NULL, null=True)
    name =         models.CharField(auto_created=True,max_length=50)

    def __str__(self):
        return self.name

