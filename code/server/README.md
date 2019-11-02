To run the Docker container, use the following commands:

docker-compose build
docker-compose down (IF REMOVING/MIGRATING ORIGINAL DB)
docker-compose up


To test, run the following commands:

docker-compose -f docker-compose.test.yml build
docker-compose -f docker-compose.test.yml up