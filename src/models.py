# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    accountid = models.AutoField(primary_key=True)
    accountnumber = models.CharField(max_length=25, blank=True, null=True)
    accountbalance = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    accountcurrency = models.CharField(max_length=3, blank=True, null=True)
    accountype = models.CharField(max_length=25, blank=True, null=True)
    custid = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='custid', blank=True, null=True)

    class Meta:
        db_table = 'account'


class Creditcard(models.Model):
    creditcardid = models.AutoField(primary_key=True)
    cctype = models.CharField(max_length=30, blank=True, null=True)
    ccnumber = models.CharField(max_length=30, blank=True, null=True)
    expirydate = models.DateField(blank=True, null=True)
    custid = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='custid', blank=True, null=True)

    class Meta:
        db_table = 'creditcard'


class Customer(models.Model):
    custid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    phonenumber = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'customer'
