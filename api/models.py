from django.db import models

# Create your models here.

# https://www.geeksforgeeks.org/decimalfield-django-models/

class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstName = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)
    lastName = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)
    title = models.CharField(db_column='title', max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    keypoints = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'
