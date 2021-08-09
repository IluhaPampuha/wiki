from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    incoming_number = models.CharField(max_length=250, blank=True)
    incoming_date = models.DateField(null=True, blank=True)
    outgoing_number = models.CharField(max_length=250, blank=True)
    outgoing_date = models.DateField(null=True, blank=True)
    number_sign = models.CharField(max_length=250, blank=True)
    date_sign = models.DateField(null=True, blank=True)
    information = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.information[:25]
