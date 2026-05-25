
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import HealthRecord
from .serializers import HealthRecordSerializer

class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        record = serializer.save()

        # Vérification des alertes
        alerts = []

        if record.heart_rate > HealthRecord.HEART_RATE_MAX:
            alerts.append(f"⚠️ Fréquence cardiaque trop élevée : {record.heart_rate} bpm")
        if record.heart_rate < HealthRecord.HEART_RATE_MIN:
            alerts.append(f"⚠️ Fréquence cardiaque trop basse : {record.heart_rate} bpm")
        if record.spo2 < HealthRecord.SPO2_MIN:
            alerts.append(f"🚨 SpO2 critique : {record.spo2}%")
        if record.temperature > HealthRecord.TEMPERATURE_MAX:
            alerts.append(f"⚠️ Fièvre détectée : {record.temperature}°C")
        if record.temperature < HealthRecord.TEMPERATURE_MIN:
            alerts.append(f"⚠️ Hypothermie détectée : {record.temperature}°C")
        if record.blood_pressure_systolic > HealthRecord.BLOOD_PRESSURE_SYSTOLIC_MAX:
            alerts.append(f"⚠️ Pression systolique élevée : {record.blood_pressure_systolic} mmHg")
        if record.sugar_rate > HealthRecord.SUGAR_RATE_MAX:
            alerts.append(f"⚠️ Glycémie élevée : {record.sugar_rate} mmol/L")

        response_data = dict(serializer.data)
        response_data['alerts'] = alerts if alerts else ["✅ Toutes les constantes sont normales"]

        return Response(response_data, status=status.HTTP_201_CREATED)
        
       