import pymysql
#import aws_credentials as rds
from base64 import b64encode

conn = pymysql.connect(
        host= "database-3.c6ojy4yqq7gm.us-east-2.rds.amazonaws.com",
        user = "admin",
        password = "Kingmaker007",
        port = 3306
        )




def get_email_password_details():
    cur=conn.cursor()
    cur.execute("SELECT EMAIL,PASSWORD FROM AWS_TEAM8_DATABASE.USER_REGISTRATION_INFO")
    User_deatils = cur.fetchall()
    return User_deatils
    
def get_image():
    cur=conn.cursor()
    cur.execute("SELECT IMAGE FROM AWS_TEAM8_DATABASE.image_table where id = 100")
    Image_file = cur.fetchall()
    Image_file = Image_file [0]
    image = b64encode(Image_file[0]).decode("utf-8")
    return image

def delet_record_function(id):
    cur=conn.cursor()
    cur.execute("DELETE FROM AWS_TEAM8_DATABASE.USER_REGISTRATION_INFO  where id ="+ " "+" ' " +str(id)+ "'")
    conn.commit()


def update_by_id(id):

    cur=conn.cursor()
    cur.execute(""" UPDATE AWS_TEAM8_DATABASE.seat_select SET Availabilty =%s WHERE id = %s """, (0, int(id)))
    conn.commit()

