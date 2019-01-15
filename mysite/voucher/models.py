from django.db import models
from django.forms import ModelForm
# Create your models here.
class Redemption(models.Model):
    name = models.CharField(max_length=30, blank=False)
    category = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name

class RedemptionForm(ModelForm):
    class Meta:
        model = Redemption
        fields = ['name', 'category', 'description']
