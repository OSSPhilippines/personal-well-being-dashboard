import dlt

class DLTData():
    def __init__(self, data):
        self.data = data
        
    def load_data_to_pipeline(self):
        pipeline = dlt.pipeline(pipeline_name="gmail_data", destination="duckdb", dataset_name="email_data")
        load_info = pipeline.run(self.data, table_name="gmail_datas")
        
    
        