from django.db import models

class employees(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.CharField(max_length=5)

    def __str__(self):
        return self.firstname


