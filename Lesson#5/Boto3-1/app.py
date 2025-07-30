from docutils.nodes import address
from flask import Flask, jsonify, request, Response
import boto3
import json
import time

app = Flask(__name__)

# Initialize the Kinesis client
kinesis_client = boto3.client('kinesis', region_name='us-east-1')
KINESIS_STREAM_NAME = 'hbd-kinesis'


def get_initial_shard_iterator():
    """Describe the stream and return a 'LATEST' shard iterator."""
    desc = kinesis_client.describe_stream(StreamName=KINESIS_STREAM_NAME)
    shard_id = desc['StreamDescription']['Shards'][0]['ShardId']
    resp = kinesis_client.get_shard_iterator(
        StreamName=KINESIS_STREAM_NAME,
        ShardId=shard_id,
        ShardIteratorType='LATEST'
    )
    return resp['ShardIterator']


@app.route('/')
def index():
    return "Welcome to the Data Streaming Demo!"


@app.route('/send', methods=['POST'])
def send_data():
    data = request.json or {}
    partition_key = data.get("partition_key", "default_key")

    # Send data to Kinesis
    response = kinesis_client.put_record(
        StreamName=KINESIS_STREAM_NAME,
        Data=json.dumps(data),
        PartitionKey=partition_key
    )

    return jsonify({"status": "Data sent to Kinesis", "response": response})


@app.route('/stream')
def stream():
    """Server‑Sent Events endpoint that streams incoming Kinesis records."""
    def event_stream():
        shard_iter = get_initial_shard_iterator()
        while True:
            resp = kinesis_client.get_records(ShardIterator=shard_iter, Limit=25)
            shard_iter = resp['NextShardIterator']
            for record in resp['Records']:
                # record['Data'] is bytes; decode and yield as SSE
                data_str = record['Data'].decode('utf-8')
                yield f"data: {data_str}\n\n"
            time.sleep(1)

    return Response(event_stream(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
