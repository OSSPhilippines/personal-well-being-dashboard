# Personal Well-being Dashboard

In recent years, there has been a significant increase in business investments in data infrastructure and capabilities. This is due to the realization of the immense value in consolidating data from various systems or sources, providing a comprehensive view of different facets of the business. The rise in popularity of various data tools aligns with the acknowledgment that data-driven insights can lead to improved decision-making and strategic planning.

Similarly, the Personal Well-being Dashboard aims to help individuals consolidate various aspects of their well-being: physical, financial, and digital. The goal of the project is not to consolidate data from various individuals, but to enable each person to access their own stats for personal consumption.

While the ultimate aim is a dashboard, the majority of the project will be focused on the data engineering aspect: ingesting, transforming, and modeling data. We aim for the process to be as automated and streamlined as possible.

We're looking for anyone who wants to contribute! No prior experience is required. You can contribute in any capacity that matches your skills and interests. We can also provide guidance if needed.

Useful links:
- [Data and Work Flow GSheet](https://docs.google.com/spreadsheets/d/1SJqBCFfW5xbAVZHrJTgjHP72mbmL_OkWQybg7wFjV3E/edit?usp=sharing)
- [Collaboration GSheet](https://docs.google.com/spreadsheets/d/1CqKHzhlnyljzaUbkVFH_9-DAhEfuX9-Owumpikoj8gM/edit?usp=sharing)
- [Facebook Group Chat](https://m.me/j/AbaL6CMK9vjk3U8l/)
- [Youtube Project Intro Videos](https://www.youtube.com/watch?v=Gup80_6nNw4&list=PLgB1IGvclbuMWY6V9Z4dgL370FpqvyAlM)

Credits are given to below repositories.
- https://github.com/jeremyephron/simplegmail (for extracting Gmail data)

## Setting up Gmail API

The only setup required is to download an OAuth 2.0 Client ID file from Google
that will authorize your application.

This can be done at: https://console.developers.google.com/apis/credentials.
For those who haven't created a credential for Google's API, after clicking the 
link above (and logging in to the appropriate account),

1. Select the project created that this authentication is for eg 'personal-well-being-dashboard'
2. Click on the "Dashboard" tab, then "Enable APIs and Services". Search for Gmail and enable.
3. Click on the Credentials tab, then "Create Credentials" > "OAuth client ID".
4. Choose the type of application you’re creating and assign it a distinctive name.
   For a straightforward setup, opt for ‘Desktop Application’.
   If you select ‘Web Application’, remember to specify an Authorized Redirect URI.
   Refer to the OAuth2 guidelines for detailed instructions.
   (See https://developers.google.com/identity/protocols/oauth2 for more infomation).
5. Back on the credentials screen, click the download icon next to the 
   credential you just created to download it as a JSON object.
6. Save this file as "client_secret.json" and place it in the root directory of 
   your application. (The `Gmail` class takes in an argument for the name of this 
   file if you choose to name it otherwise.)
7. The first time you create a new instance of the `Gmail` class, a browser window 
   will open, and you'll be asked to give permissions to the application. This 
   will save an access token in a file named "gmail-token.json", and only needs to 
   occur once.

## Installing simplegmail

Install using pip (Python3):

```bash
pip3 install simplegmail
```
