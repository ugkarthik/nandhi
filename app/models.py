from django.db import models

# Create your models here.

class Membership(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    business_location = models.TextField()
    business_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                      blank=True, null=True)
    payment_reference = models.CharField(max_length=150)
    paid_at = models.DateTimeField(blank=True, null=True)
    payment_updated_by = models.CharField(max_length=150, blank=True,
                                          null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
