import pymysql
import pandas as pds
import numpy as nup


class backend:

    def __init__(myobject, config):

        myobject.db_nm = config['db_nm']
        myobject.user = config['unm']
        myobject.password = config['pwd']
        myobject.server = config['hst']

    def make_conn(myobject):
        try:
            db_conn = None
            db_conn = pymysql.connect(
                host=myobject.server, user=myobject.user, password=myobject.password, db=myobject.db_nm)
        except Exception as err:
            print(f"Issue in database connection please check",err)
            
        return db_conn

  #  def made_bat(myobject, data, n=100):
   #   def det_get(myobject, cmmd):
    #    def made_qty(myobject, df):
            
     #       def put_dt(myobject, table_name, json_data):
                
        # myobject.table_name = table_name
      #  with cnn.cursor() as cursor:
         #   temp_df = pds.DataFrame(json_data)
          #  qry = myobject.made_qty(df=temp_df)
           # bts = myobject.made_bat(temp_df)
            #   btc = btc.replace({nup.NaN: None})
             #   dta = tuple(tuple(i) for i in btc.values)
              #  cursor.executemany(qry, dta)
              #  cnn.commit()
      #  cnn.close()
