from simplegmail import Gmail
from simplegmail.query import construct_query
import pandas as pd

gmail = Gmail()


## this is for parameter filtering
domains = ["gcash.com", "unionbankph.com"]
keywords = ["Bills Pay Receipt", "Unionbank Receipt"]

params = {
    "sender": domains,
    "subject": keywords,
}

messages = gmail.get_messages(query=construct_query(params), include_spam_trash=False) ## if you want to get all the messages, remove the query

df = []

for message in messages:
    if message.plain is not None:
        df.append({"sender": message.sender, "subject": message.subject, "body": message.plain})
    
df = pd.DataFrame(df)
 
print(df)

