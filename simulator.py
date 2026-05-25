import requests
import random
import time

API_URL = "http://127.0.0.1:8000/api/health/"

def generate_constants(anomaly=False):
    if anomaly:
        return {
            "heart_rate": random.uniform(130, 180),
            "spo2": random.uniform(85, 93),
            "temperature": random.uniform(39, 41),
            "blood_pressure_systolic": random.uniform(145, 180),
            "blood_pressure_diastolic": random.uniform(70, 90),
            "sugar_rate": random.uniform(8, 12),
        }
    return {
        "heart_rate": random.uniform(60, 100),
        "spo2": random.uniform(96, 100),
        "temperature": random.uniform(36.5, 37.5),
        "blood_pressure_systolic": random.uniform(110, 130),
        "blood_pressure_diastolic": random.uniform(60, 80),
        "sugar_rate": random.uniform(4, 6),
    }

print("🫀 Simulateur IoT démarré — envoi toutes les 3 secondes")
print("Ctrl+C pour arrêter\n")

cycle = 0
while True:
    cycle += 1
    # Toutes les 5 mesures on simule une anomalie
    anomaly = (cycle % 5 == 0)
    data = generate_constants(anomaly=anomaly)
    
    response = requests.post(API_URL, json=data)
    result = response.json()
    
    alerts = result.get('alerts', [])
    status = "🚨 ANOMALIE" if anomaly else "✅ Normal"
    
    print(f"Mesure #{cycle} [{status}]")
    print(f"  HR: {data['heart_rate']:.1f} | SpO2: {data['spo2']:.1f} | Temp: {data['temperature']:.1f}")
    print(f"  Alertes: {alerts}\n")
    
    time.sleep(3)