import time
import requests
from datetime import datetime

# Elasticsearch configuration
ELASTIC_URL = "https://a9e13e0e122d4277b8ef1c141ed139c8.us-central1.gcp.cloud.es.io:443"
ELASTIC_INDEX = "temperature-sensor"
USERNAME = "elastic"
PASSWORD = "WvePy9bMAihDgYq0joxfNrZY"

# Sensor simulation config
SENSOR_ID = "sim-temp-sensor-01"
CITY = "Toronto"
LAT = 43.7
LON = -79.42

def get_temperature():
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true"
        res = requests.get(url, timeout=5)
        data = res.json()
        return data['current_weather']['temperature']
    except Exception as e:
        print(f"[!] Error fetching temperature: {e}")
        return None

def send_to_elastic(temp):
    now = datetime.utcnow().isoformat()
    doc = {
        "@timestamp": now,
        "sensor": SENSOR_ID,
        "location": CITY,
        "temperature": temp
    }
    try:
        response = requests.post(
            f"{ELASTIC_URL}/{ELASTIC_INDEX}/_doc",
            json=doc,
            auth=(USERNAME, PASSWORD),
            headers={"Content-Type": "application/json"},
            verify=True
        )
        print(f"[+] Sent to Elastic: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[!] Error sending to Elasticsearch: {e}")

while True:
    temperature = get_temperature()
    if temperature is not None:
        print(f"🌡️  {datetime.now()} - Temp: {temperature}°C")
        send_to_elastic(temperature)
    else:
        print("[-] Failed to fetch temperature.")
    time.sleep(30)
