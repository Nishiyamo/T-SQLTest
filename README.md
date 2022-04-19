To connect to DB and make fast querys to see the schema use:
docker exec -it pedantic_mendel "bash"

Then use te next command to connect to the internal MSSQL db
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "PWD"

Inside the server you have to use:
use ATLAX360_HI_DB; that is our "Prod" db.
And do all querys to this db

All these comments, where done when experimenting with MSSQL and SQLAlchemy


ChangeLog for the code test:
Adding timeit to messure the timming of the inserted code


