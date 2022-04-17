import json
import pyodbc
import time

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
 

    def extract(self, targetFile: str):
        conn = None
        start = time.time()
        print('Starting connection and messuring time fo the transaction')
        try:
            conn = pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server}" +
                                ";SERVER=" + self._HOST + 
                                ";DATABASE=" + self._DATABASE + 
                                ";UID=" + self._USER + 
                                ";PWD=" + self._PASSWORD + 
                                ";TrustServerCertificate=Yes")
            # Insert your exercise code here
            #
            #
            # End of exercise
        except:
            print("error extracting data from sqlserver")
        finally:
            if conn:
                end = start - time.time()
                print('Clossing conection and time elapsed is %s' % end)
                conn.close()
