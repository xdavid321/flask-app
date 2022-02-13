import pymysql
#import aws_credentials as rds

conn = pymysql.connect(
        host= "database-1.cfmqfilrkvc8.us-east-2.rds.amazonaws.com",
        user = "admin",
        password = "kingmaker007",
        port = 3306
        )



cur=conn.cursor()
cur.execute("SELECT *  FROM SRINIDHI_WORKSPACE.LOGIN_INFO")
details = cur.fetchall()
for i in details:
    print(i)