from django.db import models

class Property(models.Model):

    location=models.CharField(max_length=200)

    address=models.TextField()

    price=models.PositiveIntegerField()

    TYPE_CHOICES=(
        ("apartment","apartment"),
        ("house","house"),
        ("land","land")
    )

    property_type=models.CharField(max_length=200,choices=TYPE_CHOICES,default="house")

    bedroom_count=models.PositiveIntegerField(null=True)

    square_footage=models.PositiveIntegerField()

    image=models.ImageField(upload_to="property_images",null=True,blank=True)

    phone=models.CharField(max_length=15)

    created_date=models.DateTimeField(auto_now=True)

