import requests
from prometheus_client.parser import text_string_to_metric_families
import boto3
from datetime import datetime
import time

session = boto3.session.Session(profile_name = 'os-data-dev', region_name='us-west-2')
timestream = session.client('timestream-write')

db='os-nvidia-dev'
tbl='gpu'

def proc_scrape():
    """
    calls an exposed prometheus exporter on LAN and gets all the nvidia metrics
    :return: status of the push to TimeStream
    """
    metrics = requests.get('http://192.168.2.151:9445/metrics').text
    collection_ts = int(datetime.utcnow().timestamp())
    records=[]
    for f in text_string_to_metric_families(metrics):
      if 'nvidia_' in f.name:
          for s in f.samples:
              record = {
                  "MeasureName": '_'.join([f.name, f.type]),
                  "Dimensions": [{"Name" : "host", "Value" : "phoebe"}] + [{"Name": k, "Value": str(v)} for k,v in s.labels.items()],
                  "MeasureValue": str(s.value),
                  "Time" : str(collection_ts),
                  "TimeUnit" : "SECONDS"
              }
              records.append(record)
      else:
          pass
    r = timestream.write_records(
        DatabaseName = db,
        TableName = tbl,
        Records = records
    )
    return(r)

while True:
    print(proc_scrape())
    time.sleep(30)