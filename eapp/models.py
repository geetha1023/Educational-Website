from django.db import models

# Create your models here.




class ParentRegistration(models.Model):
    parent_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    student_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.parent_name

   


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name