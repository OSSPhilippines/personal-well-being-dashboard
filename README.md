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
Please refer to their documentation for the setup guides:
- https://github.com/jeremyephron/simplegmail
- https://github.com/sladkovm/stravaio

## Setting up a free BigQuery account

1. **Initial Set-up**
    1. Sign in to your Google account.
    2. Go to [Google Cloud Console](https://console.cloud.google.com/).
    3. Select or create a new project from the project drop-down menu in the top navigation bar *(this project will be used for your BigQuery setup)*.
2. **Enable BigQuery API**
    1. Select the project from newly created project from the project drop-down menu in the top navigation bar.
    2. Enable BigQuery API by clicking [here](https://console.developers.google.com/apis/library/bigquery-json.googleapis.com/).
3. **Create a Service Account**
    1. Make sure you are logged in to your Google Cloud Console project.
    2. In the navigation menu, click `IAM & admin` and select `Service Accounts`.
    3. Click the `Create Service Account` button to set up a new Service Account.
    4. Enter a unique name for your Service Account.
    5. Select `JSON` as the Key type from the dropdown menu.
    6. Click `Create` to create the Service Account.

> [!NOTE] 
> A JSON file containing credentials for the Service Account will be downloaded to your computer. Keep this file secure, as it grants access to your BigQuery resources.

4. **Grant Permissions to Your Service Account**
    1. Click on the hamburger menu `☰` and navigate to `IAM & admin`, click on `IAM` from the left menu.
    2. Click on the `ADD` button to grant permissions to your Service Account.
    3. Paste the Service Account ID you saved earlier into the `New members` field.
    4. In the `Role` field, select `BigQuery Admin` from the dropdown menu.
    5. Additionally, ensure the `Project Browser` role is also selected to avoid errors.
    6. Click `Save` to grant the necessary permissions to your Service Account.

### Other references

* [Set up free Google BigQuery](https://levelup.gitconnected.com/how-to-use-google-bigquery-for-free-9c2a65e3a78c)
* [Setting up free BigQuery video walkthrough](https://youtu.be/BaweqxbOEM0?si=5JVaGJYmyOLyQOUe)
* [Using BigQuery Sandbox video walkthrough](https://youtu.be/JLXLCv5nUCE?si=Z7Z1ay6iue8cTT_V)