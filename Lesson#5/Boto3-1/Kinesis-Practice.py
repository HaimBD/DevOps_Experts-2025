import boto3
#
# # Defining the Kinesis client via boto3
#
client = boto3.client('kinesis')
#
# # Create Kinesis data stream
#
kinesis_name = 'hbd-kinesis'
#
# #client.create_stream(StreamName=kinesis_name, ShardCount=1, StreamModeDetails={'StreamMode': 'PROVISIONED'}, Tags={'purpose': 'exercise'})
#
# # Putting records in the Kinesis data stream
#
# client.put_record(StreamName=kinesis_name, Data='Record to put', PartitionKey='Record holder')
#
# # Getting the record in the Kinesis data stream
#
# kinesis_description = client.describe_stream(StreamName=kinesis_name)
#
# kinesis_arn = kinesis_description['StreamDescription']['StreamARN']
#
# kinesis_shard_id = kinesis_description['StreamDescription']['Shards'][0]['ShardId']
#
# shard_get_iterator = client.get_shard_iterator(StreamName=kinesis_name, ShardId=kinesis_shard_id, ShardIteratorType='LATEST')
#
# shard_iterator = shard_get_iterator['ShardIterator']
#
# print(shard_iterator)
#
# get = client.get_records(ShardIterator=shard_iterator, Limit=1, StreamARN=kinesis_arn)
#
# print(get)
#
# kinesis_resource_policy = client.get_resource_policy(ResourceARN=kinesis_arn)
#
# print(kinesis_resource_policy)

# Kinesis data stream deletion

#client.delete_stream(StreamName=kinesis_name, EnforceConsumerDeletion=True, StreamARN=kinesis_arn)