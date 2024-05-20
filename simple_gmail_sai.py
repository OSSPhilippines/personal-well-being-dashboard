from simplegmail import Gmail
from simplegmail.query import construct_query
import pandas as pd
from simplegmail.gmail_downloader import GmailDownloader
from datetime import datetime

gmail = Gmail()

gmail_downloader = GmailDownloader(gmail)

## this is for parameter filtering
domains = ["*@gcash.com", "*@unionbankph.com"]
keywords = ["Bills Pay Receipt", "Unionbank Receipt"]
start_date = datetime(2023, 2, 1)  # Start from Feb 1, 2023
end_date = datetime.now()  # Up to the current date

query = ''


query += ' OR '.join([f" from: {domain}" for domain in domains])

query += ' OR '.join([f" subject: {keyword}" for keyword in keywords])

messages = gmail.get_messages(start_date=start_date, end_date=end_date, query=query, include_spam_trash=False)

df = gmail_downloader.process_messages(messages)

df.head(10)
