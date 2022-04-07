import pymysql
#import aws_credentials as rds

conn = pymysql.connect(
        host= "database-1.cfmqfilrkvc8.us-east-2.rds.amazonaws.com",
        user = "admin",
        password = "kingmaker007",
        port = 3306
        )



cur=conn.cursor()

cur.execute("SELECT *  AWS_TEAM8_DATABASE.USER_REGISTRATION_INFO")
details = cur.fetchall()