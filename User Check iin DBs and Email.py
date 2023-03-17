import requests
import json

# Set up Mailchimp API key and list ID
MAILCHIMP_API_KEY = 'your_api_key'
MAILCHIMP_LIST_ID = 'your_list_id'

# Set up database credentials
DATABASE1_USERNAME = 'username1'
DATABASE1_PASSWORD = 'password1'
DATABASE1_NAME = 'database1'
DATABASE2_USERNAME = 'username2'
DATABASE2_PASSWORD = 'password2'
DATABASE2_NAME = 'database2'

# Set up user details
user_email = 'user@example.com'

# Check if user has a row in database 1
database1_url = f'https://database1.example.com/users/{user_email}'
response1 = requests.get(database1_url, auth=(DATABASE1_USERNAME, DATABASE1_PASSWORD))
if response1.status_code == 200:
    # User exists in database 1, check if they have a row in database 2
    database2_url = f'https://database2.example.com/users/{user_email}'
    response2 = requests.get(database2_url, auth=(DATABASE2_USERNAME, DATABASE2_PASSWORD))
    if response2.status_code == 200:
        # User exists in both databases, send email via Mailchimp
        mailchimp_url = f'https://us10.api.mailchimp.com/3.0/lists/{MAILCHIMP_LIST_ID}/members'
        mailchimp_headers = {'Authorization': f'apikey {MAILCHIMP_API_KEY}', 'Content-Type': 'application/json'}
        mailchimp_data = {
            'email_address': user_email,
            'status': 'subscribed'
        }
        response3 = requests.post(mailchimp_url, headers=mailchimp_headers, data=json.dumps(mailchimp_data))
        if response3.status_code == 200:
            print(f'Successfully sent email to {user_email}')
        else:
            print(f'Error sending email to {user_email}: {response3.content}')
    else:
        print(f'{user_email} does not have a row in {DATABASE2_NAME}')
else:
    print(f'{user_email} does not have a row in {DATABASE1_NAME}')
