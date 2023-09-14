from django.db import models
class Crud (models.Model):
    name=models.CharField(max_length=40)
    dept=models.CharField(max_length=30)
    salary=models.IntegerField()
    def __str__(self):
        return self.name
