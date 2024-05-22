!pip install requests pandas openpyxl google-cloud-bigquery

import os

# Verify the environment variable is set
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
if credentials_path:
    print(f"GOOGLE_APPLICATION_CREDENTIALS is set to: {credentials_path}")
else:
    print("GOOGLE_APPLICATION_CREDENTIALS is not set")

# Extract screen time data using Activity Watch application

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

# Use pandas and display your dataframe

import pandas as pd

# Load data from the Excel file
filename = "activitywatch_data_yourfilename.xlsx"  # Replace with your actual filename
df = pd.read_excel(filename)

# Display the first few rows of the dataframe
df.head()

# Perform any data processing you need
# Example: Group by bucket_id and count events
event_counts = df.groupby('bucket_id').size().reset_index(name='counts')
print(event_counts)

# Save processed data back to an Excel file
processed_filename = "processed_activitywatch_data.xlsx"
event_counts.to_excel(processed_filename, index=False)
print(f"Processed data saved to {processed_filename}")

# Load df to your Big Query

import pandas as pd
from google.cloud import bigquery
import os


# Read the Excel file into a DataFrame
excel_file_path = "processed_activitywatch_data.xlsx"  # Replace with your actual filename
df = pd.read_excel(excel_file_path)

# Initialize a BigQuery client
client = bigquery.Client()

# Set the destination table
dataset_id = "dataset ID"  # Replace with your dataset ID
table_id = "table ID"  # Replace with your table ID
table_ref = client.dataset(dataset_id).table(table_id)

# Define the job configuration
job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)

# Load the data into BigQuery
load_job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)

# Wait for the load job to complete
load_job.result()

print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")
