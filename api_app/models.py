from django.db import models

class HealthRecord(models.Model):
    heart_rate = models.FloatField()
    spo2 = models.FloatField()
    temperature = models.FloatField()
    blood_pressure_systolic = models.FloatField()
    blood_pressure_diastolic = models.FloatField()
    sugar_rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Record {self.timestamp} — HR: {self.heart_rate}"
    
    class Meta:
        ordering = ['-timestamp']