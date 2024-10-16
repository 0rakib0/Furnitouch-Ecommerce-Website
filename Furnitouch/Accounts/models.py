from django.db import models
from django.contrib.auth.hashers import make_password

# >>>>>>>>>>>>>>>>> for cerate superuser by email<<<<<<<<<<<<<<<<<
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class MyUserManager(BaseUserManager):
    # A custom manager to deal email as a uniqe filed
    
    
    #create user by email and password
    def _create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError("Email must be set")
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using =self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser Must have is_staff=True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError ('Superuser Must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=120)
    user_rol = (
        ('Admin','Admin'),
        ('Staff','Staff'),
        ('Factory','Factory'),
        ('Customer','Customer'),
    )
    user_type = models.CharField(
        max_length=20, 
        choices=user_rol,
        default='Customer'
        )
    is_staff = models.BooleanField(
        gettext_lazy("staff status"),
        default=False,
        help_text = gettext_lazy("Designet whether this user can Login this site")
    )
    is_active = models.BooleanField(
        gettext_lazy("Active"),
        default=True,
        help_text = gettext_lazy("designates Whether this user should be creates as active. unselect this instad of deleting accounts")
    )
    
    # def save(self, *args, **kwargs):
    #     # Hash the password before saving the object
        
    #         self.password = make_password(self.password)
    #         super().save(*args, **kwargs)
    
    
    
    USERNAME_FIELD = 'email'
    objects = MyUserManager()
    
    def __str__(self) -> str:
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=264, blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic')
    address_1 = models.TextField(max_length=300, blank=True)
    city = models.CharField(max_length=40, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user) + "'s Profile"


    # chack user Preofile fully filed or Not

    def is_fully_filed(self):
        # all field name stor in fields_name
        fields_name=[f.name for f in self._meta.get_fields()] 
        for field_name in fields_name:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True

@receiver(post_save, sender=User)
def create_profile(sender,instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()