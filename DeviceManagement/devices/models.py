from django.db import models
from employees.models import Employee
from django.utils import timezone

class Device(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    serial_number = models.CharField(max_length=255, db_index=True)
    condition_on_checkout = models.TextField(blank=True)
    condition_on_return = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "devices"
    
    def __str__(self):
        return f"{self.name} - {self.serial_number}"

class Checkout(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_at = models.DateTimeField(default=timezone.now)
    checked_in_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "checkouts"

    def __str__(self):
        status = "Checked out" if not self.checked_in_at else "Checked in"
        return f"{self.device.name} - {self.employee.name} ({status})"