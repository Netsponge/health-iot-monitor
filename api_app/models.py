from django.db import models

class HealthRecord(models.Model):
    heart_rate = models.FloatField()
    spo2 = models.FloatField()
    temperature = models.FloatField()
    blood_pressure_systolic = models.FloatField()
    blood_pressure_diastolic = models.FloatField()
    sugar_rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Seuils d'alerte
    HEART_RATE_MAX = 120
    HEART_RATE_MIN = 40
    SPO2_MIN = 95
    TEMPERATURE_MAX = 38.5
    TEMPERATURE_MIN = 35.0
    BLOOD_PRESSURE_SYSTOLIC_MAX = 140
    BLOOD_PRESSURE_DIASTOLIC_MAX = 90
    SUGAR_RATE_MAX = 7.0
    
    def __str__(self):
        return f"Record {self.timestamp} — HR: {self.heart_rate}"
    
    class Meta:
        ordering = ['-timestamp']

        