import logging
import datetime
import time
import os

# Configure logging
logging.basicConfig(filename='/app/logs/cronjob.log', level=logging.INFO)

def test_url():
    current_time = datetime.datetime.now()
    message = f"URL test executed at {current_time}"
    os.system('curl http://flask-service/')
    logging.info(message)
    print(message)
    time.sleep(5)

if __name__ == "__main__":
    test_url()