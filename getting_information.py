import pyodbc

connection_string='DSN=puc;UID=stackadmin;PWD=W0rdsarewind!'


def execute_query(query):
 try:
  conn = pyodbc.connect(connection_string)
  cursor=conn.cursor()
  cursor.execute(query)
  result_list = cursor.fetchall()
  cursor.close()
  del cursor
  conn.close()     #<--- Close the connection
 except Exception as e:
  print(traceback.format_exc())
  result_list=[]
 return result_list
