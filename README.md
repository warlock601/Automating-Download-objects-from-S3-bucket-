# Automating-Download-objects-from-S3-bucket-
We'll automate the process of downloading objects from an S3 bucket for all the existing objects in the bucket or whenever any new objects are added to the bucket.

Let say our organization has an S3 bucket and for compliance reasons, they want all of the objects in the S3 bucket to be downloaded locally and also if any new objects are added, they also get automatically downloaded. 

We will create EventBridge Event which automatically triggers a Lambda function whenever any new objects is added to the bucket and the Lambda function then using boto3 module, downloads the object locally.

### AWS Functionality used:

- AWS CloudWatch    
- EventBridge
- AWS Lambda
- IAM 
