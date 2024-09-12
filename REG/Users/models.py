
from django.db import models

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
class customusermanager(BaseUserManager):
    def create_user(self,name,email,number,password,is_superuser = False,**extra_fields):
        if not name:
            raise ValueError("Name is mandatory")
        if not email:
            raise ValueError("Email is mandatory")
        if not number:
            raise ValueError("Number is mandatory")

        email = self.normalize_email(email)
        user = self.model(name = name,email = email,number = number,password = password,is_superuser=is_superuser,
                          is_staff = True,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,name,email,number,password,**extra_fields):
        return self.create_user(name,email,number,password,True,**extra_fields)

class Details(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=200,null = False)
    email = models.EmailField(max_length=50,unique=True,null=False)
    number = models.CharField(max_length=10,null=False)
    password = models.CharField(null=True,max_length=300)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","number"]

    last_login = None

    objects = customusermanager()

class Amount(models.Model):
    Quantity = models.IntegerField(default=0)


