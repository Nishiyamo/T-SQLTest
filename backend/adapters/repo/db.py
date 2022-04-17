from sqlalchemy import create_engine

connection_string = 'mssql+pyodbc://SA:cmgYB2Zr4NJra2gRtGyjypag@127.0.0.1:1433/ATLAX360_HI_DBdriver=ODBC+Driver+17+for+SQL+Server'

db = create_engine(connection_string)