from simplegmail import Gmail
from simplegmail.query import construct_query
import pandas as pd
from simplegmail.gmail_downloader import GmailDownloader

gmail = Gmail()

gmail_downloader = GmailDownloader(gmail)

## this is for parameter filtering
domains = ["gcash.com", "unionbankph.com"]
keywords = ["Bills Pay Receipt", "Unionbank Receipt"]

params = {
    "sender": domains,
    "subject": keywords,
}

messages = gmail.get_messages(query=construct_query(params), include_spam_trash=False)

df = gmail_downloader.process_messages(messages)

df.head(10)
