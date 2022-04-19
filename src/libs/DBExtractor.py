import json
import logging
import os

import pyodbc
import time
import pandas as pd

class DBExtractor():
    def __init__(self, basepath: str, configFile: str):
        self.asset_path = basepath
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
        print('Starting connection and messuring time for the transaction')
        try:
            return pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server}" +
                                  ";SERVER=" + self._HOST +
                                  ";DATABASE=" + self._DATABASE +
                                  ";UID=" + self._USER +
                                  ";PWD=" + self._PASSWORD +
                                  ";TrustServerCertificate=Yes")
        except:
            print("error connecting to sqlserver")


    def db_close_connection(self, conn):
        if conn:
            end = self.start - time.time()
            print('Clossing conection and time elapsed is %s' % end)
            conn.close()

    def db_create_index(self, cursor, id, table, column):
        sql_str = "CREATE INDEX {id} ON {schema}.{table} ({column});"
        sql_str.format(id=id, schema=self._DATABASE, table=table, column=column)
        cursor.execute(sql_str)

    def fetch_data(self, connection):
        sql_str= """
            SELECT i.ItemId,
                i.ItemDocumentNbr,
                c.CustomerName,
                i.CreateDate,
                i.UpdateDate
            FROM {schema}.Item i 
                JOIN {schema}.Customer c ON i.CustomerId = c.CustomerId
            WHERE i.DeletedFlag = 0 AND
                i.VersionNbr = (
                    SELECT MAX(VersionNbr)
                    FROM {schema}.Item
                    WHERE DeletedFlag = 0 AND
                    ItemId = i.ItemId
                )
            ORDER BY ItemId;
        """
        sql_str.format(schema=self._DATABASE)
        try:
            df = pd.read_sql(sql_str, connection)
        except Exception as e:
            raise e

        if df:
            df['ItemSource'] = [xv if c else yv for c, xv, yv in zip(df['CustomerName'].str[:2]== '99', 'Local', 'External')]
        return df


    def dump_data(self, targetFile, data):
        f_gzip = self.asset_path + targetFile
        compression_opts = dict(method='gzip', archive_name=targetFile+'.csv')
        data.to_csv(f_csv, sep=";", line_terminator="\r\n", compression_opts=compression_opts, encoding="UTF8")


    def extract(self, targetFile: str):
        try:
            connection = self.db_connection()
            cursor = connection.cursor()
            self.db_create_index(self, cursor=cursor, id='flag', table='Item', column='DeletedFlag')
            self.db_create_index(self, cursor=cursor, id='version', table='Item', column='VersionNbr')
            cursor.close()
            data = self.fetch_data(connection)
            self.dump_data(targetFile=targetFile,data=data)
        except Exception as e:
            logging.info(e)
        finally:
            self.db_close_connection(connection)
