from flask import Flask, abort, request, Response
from influxdb_client import InfluxDBClient, Point
from influxdb_client .client.write_api import SYNCHRONOUS
import os

app = Flask(__name__)
influx_url = os.getenv('INFLUXDB_URL')
influx_token = os.getenv('INFLUXDB_TOKEN')
influx_org = os.getenv('INFLUXDB_ORG')
influx_bucket = os.getenv('INFLUXDB_BUCKET')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/sensor', methods = ['PUT'])
def record():
    if not request.json:
        abort(400)
    
    location = request.json.get('location', None)
    temperature = request.json.get('temperature', None)
    humidity = request.json.get('humidity', None)

    client = InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    
    if (location is None) or (temperature is None and humidity is None):
        abort(422)
    
    p = Point('sensor').tag('location', location)

    if (temperature is not None):
        p.field('temperature', float(temperature))
    if (humidity is not None):
        p.field('humidity', float(humidity))
    
    write_api.write(bucket=influx_bucket, record=p)

    write_api.close()
    client.close()
    return Response(status=204)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
