from django.db import models
from employees.models import Employee
from django.utils import timezone

class Device(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    serial_number = models.CharField(max_length=255, db_index=True)
    condition_on_checkout = models.TextField(blank=True)
    condition_on_return = models.TextField(blank=True)

class Checkout(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_at = models.DateTimeField(default=timezone.now)
    checked_in_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        status = "Checked out" if not self.checked_in_at else "Checked in"
        return f"{self.device.name} - {self.employee.name} ({status})"