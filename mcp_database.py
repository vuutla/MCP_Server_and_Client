import pypyodbc as odbc  # pip install pypyodbc
import pandas as pd  # pip install pandas
from credential import username, password, server, database

#server = 'dataeserver.database.windows.net'
#database = 'Employee'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
conn = odbc.connect(connection_string)

sql = '''
SELECT Empid,Empname,Dept,Location FROM Emp
'''
cursor = conn.cursor()
cursor.execute(sql)

dataset = cursor.fetchall()
columns = [column[0] for column in cursor.description]
df = pd.DataFrame(dataset, columns = columns)
print(df)
