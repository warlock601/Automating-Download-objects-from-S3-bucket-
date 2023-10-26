import boto3
from boto3.session import Session

ACCESS_KEY_ID = 'AKIAWCPCNPNPFYWFNTGM'
SECRET_KEY = '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'

Session = Session(aws_access_key_id=ACCESS_KEY_ID,
                  aws_secret_access_key=SECRET_KEY)

s3= Session.resource('s3')

bucket = 'binnybucket'

my_bucket = s3.Bucket(bucket)

for s3_files in my_bucket.objects.all():
    print("downloading")

my_bucket.download_file('Docker.txt','./Docker.txt')
print('Downloaded')    
