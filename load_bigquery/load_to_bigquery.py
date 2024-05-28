import pandas as pd
from google.cloud import bigquery

def load_data_to_bigquery(df, dataset_id, table_id):
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    load_job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    load_job.result()  # Wait for the job to complete
    print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")

if __name__ == "__main__":
    # Example usage:
    excel_file_path = "processed_activitywatch_data.xlsx"  # Replace with your actual filename
    dataset_id = "your_dataset_id"  # Replace with your dataset ID
    table_id = "your_table_id"  # Replace with your table ID

    df = pd.read_excel(excel_file_path)
    load_data_to_bigquery(df, dataset_id, table_id)
