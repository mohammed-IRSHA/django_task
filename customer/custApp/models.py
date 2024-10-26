from django.db import models

# Create your models here.
class customer(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    addres=models.TextField()
    phone=models.CharField(max_length=10)
    update_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class order(models.Model):
    orid=models.IntegerField(primary_key=True)
    orname=models.CharField(max_length=100)
    cust=models.ForeignKey(customer,on_delete=models.CASCADE)
class user(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    phone=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
class loginform(models.Model):
    lname=models.CharField(max_length=100)
    passkey=models.CharField(max_length=30)
    