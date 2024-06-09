# LambdaEmailSender


Description: LambdaEmailSender is a serverless email application built using AWS Lambda, Amazon SES, and Amazon S3. It automates the process of sending mass emails to a large audience by triggering Lambda functions in response to new CSV files uploaded to an S3 bucket. This project provides a cost-effective and scalable solution for sending bulk emails while leveraging the power of serverless computing and AWS cloud services.

Steps to perform the mini-porject.

1.2 Set up AWS IAM:
Go to the IAM Dashboard.
Create an IAM role with permissions to access S3 and SES.
Attach the role to your Lambda function to grant it necessary permissions.

1.3 Set up Amazon SES:
Go to the Amazon SES Console.
Follow the instructions to verify the email addresses you want to send emails from and to.

2. Develop Lambda Function:
2.1 Create a New Lambda Function:
Go to the AWS Lambda Console.
Click on "Create function".
Choose "Author from scratch" and configure the function settings (e.g., name, runtime).
Click on "Create function".
2.2 Write Lambda Function Code:
Write Python code to handle S3 events, parse CSV files, and send emails using SES.
Use the AWS SDK (boto3) to interact with AWS services.
Ensure your Lambda function is properly structured and handles errors gracefully.
You can use a template like the one provided earlier in this conversation and customize it for your requirements.

2.3 Test the Lambda Function:
Test the Lambda function with sample S3 events and CSV files to ensure it works as expected.
Monitor the execution logs in the AWS CloudWatch Logs console for any errors or issues.

3. Configure S3 Event Trigger:
3.1 Set up S3 Bucket:
Go to the Amazon S3 Console.
Create an S3 bucket to store CSV files containing email lists.

3.2 Configure S3 Event Trigger:
Select the bucket you created.
Go to the "Properties" tab and click on "Event notifications".
Add a new event notification configuration to trigger the Lambda function whenever a new CSV file is uploaded to the bucket.

4. Test the Application:
4.1 Upload CSV File to S3:
Upload a sample CSV file containing email addresses to the S3 bucket configured in the previous step.

4.2 Monitor Lambda Function Logs:
Go to the AWS CloudWatch Logs Console.
Monitor Lambda function execution logs to ensure it is triggered and executes successfully.

4.3 Verify Email Delivery:
Check the email inbox of the recipients specified in the CSV file to verify that emails are delivered successfully.

**************************************

**Room of improvement**

This project's scope is local i.e. in sandbox as of now.
In a sandbox environment, you can use all of the features offered by Amazon SES; however, certain sending limits and restrictions apply. When you're ready to move out of the sandbox, submit a request for production access. 

**************************************


