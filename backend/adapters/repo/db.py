from sqlalchemy import create_engine

server = '127.0.0.1:1433'
database = 'ATLAX360_HI_DB'
driver = 'ODBC+Driver+17+for+SQL+Server'
user = 'SA'
password = 'cmgYB2Zr4NJra2gRtGyjypag'
connection_string = f'mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}'

engine = create_engine(connection_string)
db = engine.connect()
