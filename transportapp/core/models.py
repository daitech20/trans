from django.db import models

# Create your models here.
class Information(models.Model):
    from_street1 = models.CharField(max_length=100)
    from_street2 = models.CharField(max_length=100)
    from_city = models.CharField(max_length=100)
    from_state = models.CharField(max_length=3)
    from_zip = models.CharField(max_length=10)
    from_country = models.CharField(max_length=20)
    from_phone = models.CharField(max_length=20)

    to_street1 = models.CharField(max_length=100)
    to_street2 = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    to_state = models.CharField(max_length=3)
    to_zip = models.CharField(max_length=10)
    to_country = models.CharField(max_length=20)
    to_phone = models.CharField(max_length=20)

    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
