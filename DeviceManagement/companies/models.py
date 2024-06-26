from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    location = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "companies"
        
    def __str__(self):
        return self.name
    

