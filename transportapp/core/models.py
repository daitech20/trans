from django.db import models


COUNTRY = (
    ("HK", "Hong Kong"),
    ("VN", "Viet Nam"),
    ("JP", "Japan "),
    ("CA", "Canada"),
    ("AU", "Australia"),
    ("AS", "American Samoa"),
    ("US", "United States"),
    ("CN", "China"),
)

# Create your models here.
class Information(models.Model):
    from_street1 = models.CharField(max_length=100)
    from_street2 = models.CharField(max_length=100)
    from_zip = models.CharField(max_length=10)
    from_country = models.CharField(max_length=20, choices=COUNTRY)
    from_phone = models.CharField(max_length=20)

    to_street1 = models.CharField(max_length=100)
    to_street2 = models.CharField(max_length=100)
    to_zip = models.CharField(max_length=10)
    to_country = models.CharField(max_length=20, choices=COUNTRY)
    to_phone = models.CharField(max_length=20)

    length = models.FloatField(default=1)
    width = models.FloatField(default=1)
    height = models.FloatField(default=1)
    weight = models.FloatField(default=1)
