To connect to DB and make fast querys to see the schema use:
docker exec -it pedantic_mendel "bash"

Then use te next command to connect to the internal MSSQL db
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "PWD"
