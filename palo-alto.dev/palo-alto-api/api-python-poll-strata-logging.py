# This is not a working script. Strata Logging does not have an API. Keeping this for future reference.

import requests
import json
import time
import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision

# Palo Alto Networks API setup
ACCESS_TOKEN = "your_access_token_here"
BASE_URL = "https://api.logging-service.paloaltonetworks.com"
HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}

# InfluxDB setup
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "your_influx_token_here"
ORG = "your_org"
BUCKET = "strata_metrics"

# Initialize client
influx = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=ORG)
write_api = influx.write_api(write_options=None)

# Define time range and queries
time_filter = "receive_time >= now() - 7d"
queries = {
    "url_transactions": f"SELECT COUNT(*) as total FROM traffic WHERE app = 'web-browsing' AND {time_filter}",
    "adware_spyware": f"SELECT COUNT(*) as total FROM threat WHERE subtype IN ('adware','spyware') AND {time_filter}",
    "vulnerabilities": f"SELECT COUNT(*) as total FROM threat WHERE subtype='vulnerability' AND {time_filter}"
}

def run_query(query):
    resp = requests.post(f"{BASE_URL}/logquery", headers=HEADERS, data=json.dumps({"query": query}))
    job_id = resp.json().get("jobId")
    time.sleep(5)
    result = requests.get(f"{BASE_URL}/logquery/{job_id}", headers=HEADERS).json()
    return result['data'][0]['total'] if result.get('data') else 0

# Run all queries
results = {
    "url_transactions": run_query(queries["url_transactions"]),
    "adware_spyware": run_query(queries["adware_spyware"]),
    "vulnerabilities": run_query(queries["vulnerabilities"])
}

# Write data points to InfluxDB
timestamp = datetime.datetime.utcnow()
for metric, value in results.items():
    point = (
        Point("strata_metrics")
        .tag("metric", metric)
        .field("value", value)
        .time(timestamp, WritePrecision.NS)
    )
    write_api.write(bucket=BUCKET, org=ORG, record=point)

print(f"Metrics written to InfluxDB bucket '{BUCKET}' at {timestamp}")
