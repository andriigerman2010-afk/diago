from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    group = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.name}: {self.role.name}'