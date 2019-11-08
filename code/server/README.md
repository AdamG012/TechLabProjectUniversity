Back-end API server:
- A containerised server used to host the Django back-end API
- Located in /code/server/
- Server settings are in /code/server/server/settings.py
- Main application code is written in /code/server/trends/
- Can be run using docker-compose. The commands are:
    - "docker-compose -f docker-compose.yml build" (First time or environment update)
    - "docker-compose -f docker-compose.yml up" (To run the server)
    - "docker-compose -f docker-compose.yml down" (To reset the server)

MySQL Database server:
- A containerised server used to host the MySQL database, which is used by the Django back-end API.
- Located in /code/server/
- Can be run using docker-compose. The commands are:
    - "docker-compose -f docker-compose-db.yml build" (First time or environment update)
    - "docker-compose -f docker-compose-db.yml up" (To run the server)
    - "docker-compose -f docker-compose-db.yml down" (To reset the server and clear the database)
    
Unit test container
- A containerised environment used to run the unit tests of the code.
- Located in /code/server/. Unit tests are written in /code/server/tests/
- Can be run using docker-compose. The commands are:
    - "docker-compose -f docker-compose-test.yml build" (First time or environment update)
    - "docker-compose -f docker-compose-test.yml up" (To run the tests)