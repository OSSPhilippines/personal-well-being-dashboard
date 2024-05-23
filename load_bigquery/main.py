import pandas as pd
from datetime import datetime
from extract_activitywatch_data import fetch_activitywatch_data, save_to_excel
from load_to_bigquery import load_data_to_bigquery

def process_data(filename):
    df = pd.read_excel(filename)
    # Perform any data processing you need
    event_counts = df.groupby('bucket_id').size().reset_index(name='counts')
    processed_filename = "processed_activitywatch_data.xlsx"
    event_counts.to_excel(processed_filename, index=False)
    print(f"Processed data saved to {processed_filename}")
    return processed_filename

if __name__ == "__main__":
    # Step 1: Extract data
    data = fetch_activitywatch_data()
    raw_filename = f"activitywatch_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    save_to_excel(data, raw_filename)
    print(f"Data saved to {raw_filename}")

    # Step 2: Process data
    processed_filename = process_data(raw_filename)

    # Step 3: Load data to BigQuery
    dataset_id = "your_dataset_id"  # Replace with your dataset ID
    table_id = "your_table_id"  # Replace with your table ID
    df = pd.read_excel(processed_filename)
    load_data_to_bigquery(df, dataset_id, table_id)
