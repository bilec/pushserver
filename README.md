# pushserver

Simple server that receives PUT requests and writes them to InfluxDB.

## Request
```http
### Expect code 204
POST http://localhost:5000/record
   Content-Type: application/json

   {
     "location": "bedroom",
     "temperature": "20.5",
     "humidity": "54.2"
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
