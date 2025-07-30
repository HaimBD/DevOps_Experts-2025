import boto3

# Initialize a session using your profile
session = boto3.Session()
s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-cool-bucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'
})
s3.upload_file('local-file.txt', 'my-cool-bucket', 'uploaded-file.txt')
response = s3.list_objects_v2(Bucket='my-cool-bucket')
for obj in response['Contents']:
    print(obj['Key'])
s3.download_file('my-cool-bucket', 'uploaded-file.txt', 'downloaded-file.txt')
s3.delete_object(Bucket='my-cool-bucket', Key='uploaded-file.txt')
s3.delete_bucket(Bucket='my-cool-bucket')


ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-0abcdef1234567890',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='MyKeyPair'
)
print(f'Launched EC2 Instance ID: {instance[0].id}')

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f'Instance ID: {instance["InstanceId"]}, State: {instance["State"]["Name"]}')

ec2.stop_instances(InstanceIds=['i-0123456789abcdef0'])
print('Stopped instance i-0123456789abcdef0')

ec2.terminate_instances(InstanceIds=['i-0123456789abcdef0'])
print('Terminated instance i-0123456789abcdef0')


dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='MyTable',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
print(f'Created DynamoDB Table: {table.name}')

table = dynamodb.Table('MyTable')
table.put_item(
    Item={
        'id': '123',
        'name': 'John Doe',
        'age': 30
    }
)
print('Inserted item into MyTable')


response = table.get_item(
    Key={
        'id': '123'
    }
)
item = response['Item']
print(f'Retrieved item: {item}')


table.update_item(
    Key={
        'id': '123'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 31
    }
)
print('Updated item in MyTable')

table.delete_item(
    Key={
        'id': '123'
    }
)
print('Deleted item from MyTable')

table.delete()
print('Deleted DynamoDB Table: MyTable')


iam = boto3.client('iam')
iam.create_user(UserName='newuser')
print('Created IAM User: newuser')

iam.attach_user_policy(
    UserName='newuser',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
)
print('Attached S3FullAccess policy to newuser')

response = iam.create_access_key(UserName='newuser')
access_key = response['AccessKey']['AccessKeyId']
secret_key = response['AccessKey']['SecretAccessKey']
print(f'Created access key for newuser: {access_key}')

iam.delete_user(UserName='newuser')
print('Deleted IAM User: newuser')