import requests
import pandas as pd
from datetime import datetime

def fetch_activitywatch_data():
    base_url = "http://localhost:5600/api/0"
    buckets_url = f"{base_url}/buckets"
    
    response = requests.get(buckets_url)
    response.raise_for_status()  # Ensure we raise an error for bad responses
    
    buckets = response.json()
    print("Buckets:", buckets)  # Debug print to inspect the response
    
    all_events = []
    for bucket_id, bucket in buckets.items():  # Iterate over dictionary items
        events_url = f"{buckets_url}/{bucket_id}/events"
        response = requests.get(events_url)
        response.raise_for_status()
        events = response.json()
        for event in events:
            event['bucket_id'] = bucket_id
            all_events.append(event)
    
    return all_events

def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    # Convert timestamps to timezone-unaware
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.tz_localize(None)
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    data = fetch_activitywatch_data()
    filename = f"activitywatch_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    save_to_excel(data, filename)
    print(f"Data saved to {filename}")
