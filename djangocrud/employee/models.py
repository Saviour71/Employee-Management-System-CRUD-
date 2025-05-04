from django.db import models


class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=100)
    employee_email = models.CharField(max_length=80)
    employee_contact = models.CharField(max_length=20)

    def __str__(self):
        return self.employee_name
