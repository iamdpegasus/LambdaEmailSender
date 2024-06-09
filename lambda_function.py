import json
import boto3
import pandas as pd
import logging
import time
import os

# Initialize AWS clients for S3 and SES
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')

# Define your S3 bucket name
BUCKET_NAME = 'your-bucket-name'

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
# Log the incoming event
logger.info('Received event: %s', json.dumps(event, indent=2))

try:
# Extract bucket and file information from the event
bucket_name = event['Records'][0]['s3']['bucket']['name']
file_name = event['Records'][0]['s3']['object']['key']

# Log the bucket and file information
logger.info('Bucket: %s, File: %s', bucket_name, file_name)

# Ensure the event is from the correct bucket
if bucket_name == BUCKET_NAME:
retries = 3
file_content = None
for i in range(retries):
try:
# Fetch the file from S3
response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
file_content = response['Body'].read()
break
except s3_client.exceptions.NoSuchKey:
logger.info('File not found, retrying in 5 seconds...')
time.sleep(5)
continue

# Check if the file was fetched successfully
if not file_content:
raise Exception('File not found after retries')

# Determine the file extension
file_extension = os.path.splitext(file_name)[1].lower()

# Save the file content to a temporary file
temp_file_path = f'/tmp/temp_file{file_extension}'
with open(temp_file_path, 'wb') as temp_file:
temp_file.write(file_content)

# Read the file using pandas
if file_extension == '.csv':
df = pd.read_csv(temp_file_path)
elif file_extension in ['.xls', '.xlsx']:
df = pd.read_excel(temp_file_path)
else:
raise Exception('Unsupported file type')

# Iterate over the rows and send emails
for _, row in df.iterrows():
email = row['email'].strip() # Adjust the column name if necessary
send_email(email)

# Log success message
logger.info('Emails sent successfully!')

return {
'statusCode': 200,
'body': json.dumps('Emails sent successfully!')
}
else:
# Log incorrect bucket error
logger.error('Incorrect S3 bucket')

return {
'statusCode': 400,
'body': json.dumps('Incorrect S3 bucket')
}
except KeyError as e:
logger.error('KeyError: %s', str(e))
return {
'statusCode': 400,
'body': json.dumps(f'Missing key in event: {str(e)}')
}
except Exception as e:
logger.error('Error: %s', str(e))
return {
'statusCode': 500,
'body': json.dumps(f'Error: {str(e)}')
}

def send_email(email):
# Send an email using AWS SES
response = ses_client.send_email(
Source='iamshreeku@gmail.com',
Destination={
'ToAddresses': [email]
},
Message={
'Subject': {
'Data': 'Hello from AWS Lambda',
'Charset': 'UTF-8'
},
'Body': {
'Text': {
'Data': 'This is a test email sent from AWS Lambda.',
'Charset': 'UTF-8'
}
}
}
)
