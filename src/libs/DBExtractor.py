import json
import logging

import pyodbc
import time
import pandas as pd

class DBExtractor():
    def __init__(self, configFile: str):
        f = open(configFile)
        data = json.load(f)
        
        self._HOST = data["HOST"]
        self._PORT = data["PORT"]
        self._DATABASE = data["DATABASE"]
        self._USER = data["USER"]
        self._PASSWORD = data["PASSWORD"]
        
        f.close()


    def db_connection(self):
        conn = None
        self.start = time.time()
        print('Starting connection and messuring time fo the transaction')
        try:
            return pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server}" +
                                  ";SERVER=" + self._HOST +
                                  ";DATABASE=" + self._DATABASE +
                                  ";UID=" + self._USER +
                                  ";PWD=" + self._PASSWORD +
                                  ";TrustServerCertificate=Yes")
        except:
            print("error extracting data from sqlserver")


    def db_close_connection(self, conn):
        if conn:
            end = self.start - time.time()
            print('Clossing conection and time elapsed is %s' % end)
            conn.close()

    def db_create_index(self, cursor, id, table, column):
        sql_str = " CREATE INDEX {id} ON {schema}.{table} ({column}); "
        sql_str.format(id=id, schema=self._DATABASE, table=table, column=column)
        cursor.execute(sql_str)

    # def fetch_data(self):
    #     sql_str= """
    #
    #     """
    #
    #
    def dump_to_csv(self, targetFile, data):
        basepath = os.getcwd()
    # todo create and dump to csv data

    def gzip_csv(self, csv):
# todo gzip csv

    # Main fn for this class
    def extract(self, targetFile: str):
        try:
            connection = self.db_connection()
            cursor = connection.cursor()
            self.db_create_index(self, cursor=cursor, id='flag', table='Item', column='DeletedFlag')
            self.db_create_index(self, cursor=cursor, id='version', table='Item', column='VersionNbr')

        except Exception as e:
            logging.ERROR(e)
        finally:
            self.db_close_connection(connection)
