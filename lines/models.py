
#django
from django.db import models

# Create your models here.



class part(models.Model):
    """Part model."""
    """user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)"""
    id = models.AutoField(primary_key=True)
    code2d = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class st1(models.Model):
    """St1 model"""
    id = models.AutoField(primary_key=True)
    partid = models.ForeignKey(part,on_delete=models.CASCADE)
    judge=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    valor1 = models.FloatField()
    valor2 = models.FloatField()
    valor3 = models.FloatField()
    valor4 = models.FloatField()




    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)
