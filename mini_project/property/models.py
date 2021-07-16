from django.db import models
from account.models import User

# Create your models here.
class Property(models.Model):
    TYPE_CHOICES = (
            ("FLAT", "Flat"),
            ("VILLA", "Villa"),
            ("BUNGLOW", "Bunglow"),
            ("COTTAGE", "Cottage"),
    )
    BHK_OR_RK_CHOICE = (
        ("BHK", "BHK"),
        ("RK", "RK"),
    )
    type = models.CharField(max_length=8, 
        choices = TYPE_CHOICES,
        default = "FLAT",
    )
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    under_construction = models.BooleanField(verbose_name = 'Under Construction')
    rera = models.BooleanField(verbose_name = 'RERA')
    bhk_no = models.IntegerField(verbose_name = 'BHK No')
    bhk_or_rk = models.CharField(max_length=3, 
        choices = BHK_OR_RK_CHOICE,
        default = "BHK",
        verbose_name = 'BHK or RK',
    )
    square_ft = models.FloatField(verbose_name = 'Square Feet')
    ready_to_move = models.BooleanField(verbose_name = 'Ready To Move')
    resale = models.BooleanField(verbose_name = 'Resale')
    address = models.CharField(max_length=200, verbose_name = 'Address')
    latitude = models.FloatField(verbose_name = 'Longitude')
    longitude = models.FloatField(verbose_name = 'Latitude')
    cost_estimated = models.FloatField(verbose_name = 'Cost Estimated', null=True, blank=True)

class Favourite_Property(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

class Faq_Property(models.Model):
    faq_posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    question = models.CharField(max_length=300, verbose_name = 'Question')
    answer = models.CharField(max_length=300, verbose_name = 'Answer', blank= True)
    