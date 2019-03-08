from django.db import models
from django.core.validators import MinLengthValidator

class contact(models.Model):
    first_name = models.CharField(
        max_length=60,
    )

    last_name = models.CharField(
        max_length=60,
    )

    email  = models.EmailField( 
        max_length=128,
    )

    phone_number = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        blank=True, 
        null=True
    )

    message = models.TextField(
        blank=True, 
        null=True
    )
