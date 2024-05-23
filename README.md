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
- https://github.com/sladkovm/stravaio (might be used in the future)

## Setting up BigQuery API

1. **Initial Set-up**
    1. Sign in to your Google account.
    2. Go to [Google Cloud Console](https://console.cloud.google.com/).
    3. Select or create a new project from the project drop-down menu in the top navigation bar *(This project will be used for your BigQuery setup.
    Optionally, you may name the project 'personal-well-being-dashboard')*.
2. **Enable BigQuery API**
    1. Select the project from newly created project from the project drop-down menu in the top navigation bar.
    2. Enable BigQuery API by clicking [here](https://console.cloud.google.com/apis/library/bigquery.googleapis.com).
3. **Create a Service Account**
    1. Make sure you are logged in to your Google Cloud Console project.
    2. In the navigation menu, click `IAM & admin` and select `Service Accounts`.
    3. Click the `Create Service Account` button to set up a new Service Account.
    4. Enter a unique name for your Service account name and Service account ID.
       For example, you may assign 'personal-well-being-dashboard' to Service account name,
       and 'main-service-account' to Service account ID. This will result to 'main-service-account@personal-well-being-dashboard.iam.gserviceaccount.com'
    5. Click `Next` for steps 2 and 3, which are optional.
    6. On the right side of the created service account, click the three-dot button for the actions.
    7. Click manage permissions.
    8. Click `KEYS`, `ADD KEY`, `Create new key`, `JSON`, then `Create`.

> [!NOTE] 
> A JSON file containing credentials for the Service Account will be downloaded to your computer. Keep this file secure, as it grants access to your BigQuery resources.

4. **Grant Permissions to Your Service Account**
    1. Click on the hamburger menu `☰` and navigate to `IAM & admin`, click on `IAM` from the left menu.
    2. Click on the `GRANT ACCESS` button to grant permissions to your Service Account.
    3. Paste eg 'main-service-account@personal-well-being-dashboard.iam.gserviceaccount.com' into the `New principals` field.
    4. In the `Role` field, select `BigQuery Admin` from the dropdown menu.
    5. Click `Save` to grant the necessary permissions to your Service Account.

### Other references

* [Set up free Google BigQuery](https://levelup.gitconnected.com/how-to-use-google-bigquery-for-free-9c2a65e3a78c)
* [Setting up free BigQuery video walkthrough](https://youtu.be/BaweqxbOEM0?si=5JVaGJYmyOLyQOUe)
* [Using BigQuery Sandbox video walkthrough](https://youtu.be/JLXLCv5nUCE?si=Z7Z1ay6iue8cTT_V)

> [!NOTE] 
> Let's consider replacing the above references in the future with official documentation from BigQuery

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
