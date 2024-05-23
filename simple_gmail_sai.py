from simplegmail import Gmail
from simplegmail.query import construct_query
import pandas as pd
from simplegmail.gmail_downloader import GmailDownloader
from datetime import datetime

gmail = Gmail()

gmail_downloader = GmailDownloader(gmail)

def format_query(domains, keywords = None, start_date = None, end_date = None):
    query = ''
    if start_date:
        query += f' after:{start_date.strftime("%Y/%m/%d")}'
        
    if end_date:
        query += f' before:{end_date.strftime("%Y/%m/%d")}'
        
  
    query += ' OR '.join([f" from:{domain}" for domain in domains] + [f" to:{domain}" for domain in domains])

    return query
    

## this is for parameter filtering
domains = ["gcash.com", "unionbankph.com"]
keywords = []
start_date = datetime(2023, 2, 1)  # Start from Feb 1, 2023
end_date = datetime.now()  # Up to the current date

query = format_query(domains, keywords, start_date, end_date)


print(query)

messages = gmail.get_messages(start_date=start_date, end_date=end_date, query=query, include_spam_trash=False)

df = gmail_downloader.process_messages(messages)

df.head(50)
