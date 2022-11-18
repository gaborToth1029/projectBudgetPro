from email.policy import default
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
      if not email:
          raise ValueError('Users must have an email address')

      email = self.normalize_email(email)
      email = email.lower()    

      user = self.model(
            first_name = first_name,
            last_name = last_name,
            email= email,
            
     )

      user.set_password(password)
      user.save(using=self._db)
      
      return user

    def create_superuser(self, first_name, last_name, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password,
            
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user 

class MyUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique = True, max_length=255)
    is_active= models.BooleanField(default = False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self) -> str:
        return self.email
        
