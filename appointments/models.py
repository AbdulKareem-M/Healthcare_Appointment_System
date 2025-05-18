from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience_years = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    
    def clean(self):
        # Prevent booking for past dates
        if self.date and self.date < timezone.now().date():
            raise ValidationError("You cannot book an appointment in the past.")


    def __str__(self):
        return f"Appointment with Dr. {self.doctor.name} on {self.date} at {self.time}"
