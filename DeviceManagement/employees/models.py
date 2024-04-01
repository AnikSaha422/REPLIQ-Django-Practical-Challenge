from django.db import models
from companies.models import Company


# Create your models here.
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    job_title = models.CharField(max_length=100)
    joined_on = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "employees"
        
    
    def __str__(self):
        return self.name
    
