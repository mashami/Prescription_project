from django.db import models

# Create your models here.

class DoctorM(models.Model):
    # id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=True)
    DoctorName =models.CharField(max_length=100, blank=True , null=False)
    medicine=models.CharField(max_length=100, default='none')
    Diseases=models.CharField(max_length=100, default=None)
    Date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Doctor:{self.DoctorName}"