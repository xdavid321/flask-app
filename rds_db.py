import pymysql
#import aws_credentials as rds

conn = pymysql.connect(
        host= "database-1.cfmqfilrkvc8.us-east-2.rds.amazonaws.com",
        user = "admin",
        password = "kingmaker007",
        port = 3306
        )

def insert_details(fName, lName,email,password):
    cur=conn.cursor()
    cur.execute("INSERT INTO SRINIDHI_WORKSPACE.LOGIN_INFO(FIRST_NAME,LAST_NAME,EMAIL,PASSWORD) VALUES (%s,%s,%s,%s)", (fName, lName,email,password))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM SRINIDHI_WORKSPACE.LOGIN_INFO")
    details = cur.fetchall()
    return details

def get_email_password_details():
    cur=conn.cursor()
    cur.execute("SELECT EMAIL,PASSWORD FROM SRINIDHI_WORKSPACE.LOGIN_INFO")
    User_deatils = cur.fetchall()
    return User_deatils