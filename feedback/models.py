from django.db import models

class Feedback(models.Model):
    user_name = models.CharField( 
        max_length=60
    )

    #phone number should be 10 but it is given in problem that its max_length should be 60
    phone_number = models.CharField( 
        max_length=60
    )

    email  = models.EmailField( 
        max_length=128,
    )

    location = models.TextField(
        max_length = 60
    )

    feedback = models.TextField(
        max_length = 500
    )
