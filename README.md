# pushserver

[![Docker Repository on Quay](https://quay.io/repository/speed5719/pushserver/status "Docker Repository on Quay")](https://quay.io/repository/speed5719/pushserver)
[![Docker image build](https://github.com/bilec/pushserver/actions/workflows/docker_image_build.yml/badge.svg)](https://github.com/bilec/pushserver/actions/workflows/docker_image_build.yml)

Simple server that receives PUT requests and writes them to InfluxDB.

## Request
```http
### Expect code 204
PUT http://localhost:5000/sensor
Content-Type: application/json

{
  "location": "bedroom",
  "temperature": "20.5",
  "humidity": "54.2"
}

### Expect code 422
PUT http://localhost:5000/sensor
Content-Type: application/json

{ 
  "temperature": "20.5"
}
```

## Docker image
https://quay.io/repository/speed5719/pushserver

## Run
```shell
docker run -d -p 5000:5000 -e INFLUXDB_URL='' \
-e INFLUXDB_TOKEN='' \
-e INFLUXDB_ORG='' \
-e INFLUXDB_BUCKET='' \
quay.io/speed5719/pushserver:latest
```
