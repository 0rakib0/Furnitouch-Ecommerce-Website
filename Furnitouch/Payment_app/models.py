from django.db import models
from Accounts.models import User
# Create your models here.

class Billing_address(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=267, blank=True)
    address_2 = models.CharField(max_length=267, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True)
    city    = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=20, blank=True)


    def __str__(self) -> str:
        return str(self.user.email)+ ' Billing address'
    
    def is_fully_filled(self):
        Field_name = [f.name for f in self._meta.get_fields()]


        for field_name in Field_name:
            value = getattr(self, field_name)

            if value is None or value=='':
                return False
        return True
    
    class Meta:
        verbose_name_plural = 'Billing Address'




