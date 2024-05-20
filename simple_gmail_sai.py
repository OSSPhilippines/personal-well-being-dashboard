from simplegmail import Gmail
from simplegmail.query import construct_query
import pandas as pd
from simplegmail.gmail_downloader import GmailDownloader
from datetime import datetime

gmail = Gmail()

gmail_downloader = GmailDownloader(gmail)

## this is for parameter filtering
domains = ["gcash.com", "unionbankph.com"]
keywords = ["Bills Pay Receipt", "Unionbank Receipt"]

params = {
    "sender": domains,
    "subject": keywords,
}

start_date = datetime(2024, 2, 1)  # Start from Feb 1, 2024
end_date = datetime.now()  # Up to the current date

messages = gmail.get_messages(after=start_date, before=end_date, query=construct_query(params), include_spam_trash=False)

df = gmail_downloader.process_messages(messages)

df.head(10)
