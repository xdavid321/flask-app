# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:02:51 2020

@author: hp
"""

from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file
app = Flask(__name__)
import rds_db as db
import pymysql
from base64 import b64encode


@app.route('/',methods = ['POST','GET'])
def home():
    details = db.get_movie_poster()
    image_list = []
    Dummy_list =[]
    for i in details:
            images = b64encode(i[1]).decode("utf-8")
            Dummy_list.append(images)
            Dummy_list.append(i[0])
            Dummy_list.append(i[2])
            image_list.append(Dummy_list)
            Dummy_list =[]
    return render_template('homePage.html', data = image_list) 

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_movie_detailed_view(id):
    all_file = db.fetch_movie_detailed_view(id)
    for i in all_file:
            ID = i[0]
            movie_front_poster= b64encode(i[1]).decode("utf-8")
            movie_name = i[2]
            movie_description  = i[3]
            movie_bg_image = b64encode(i[4]).decode("utf-8")
            movie__rating = i[5]
            movie_genere = i[6]
            #actor1_image = b64encode(i[7]).decode("utf-8")
            actor1_name = i[8]
            movie_trailer_link= i[9]
   
    return render_template('moviedeatildview.html',ID = ID,                    
                                        movie_front_poster=movie_front_poster, 
                                        movie_name =movie_name,
                                        movie_description= movie_description,
                                        movie_bg_image = movie_bg_image ,
                                        movie__rating = movie__rating,
                                        movie_genere =movie_genere,
                                        #actor1_image = actor1_image,
                                        actor1_name =actor1_name,
                                        movie_trailer_link = movie_trailer_link )



@app.route('/login')
def index():
    return render_template('login.html')



@app.route('/loginInfo',methods = ['POST','GET'])
def login():  
    if request.method == 'POST':
        email_html = request.form['email']
        password_html = request.form['password']
        User_details = db.get_email_password_details()
        for i in User_details:
               emails_temp = (i[0])
               password_temp = (i[1])
               if email_html == emails_temp and password_html == password_temp :
                return 'success'
        return render_template("wrongpwd.html")           
     
            
    
@app.route('/signup')
def signup():
    return render_template('registration.html')



@app.route('/registrationInfo',methods = ['POST','GET'])
def registration():
    if request.method == 'POST':
        fName = request.form['fName']
        lName = request.form['lName']
        email = request.form['email']
        password = request.form['password']
        db.insert_details(fName, lName,email,password)
        return render_template("regSuc.html")
    #return redirect(url_for("index"))


@app.route('/registrationInfox',methods = ['POST','GET'])
def Index1():
    print('----------------111111111-----------------------------')
    details = db.get_details()
 
    print(details)
    return render_template('Registration_information.html', employee = details)

@app.route('/imagefox',methods = ['POST','GET'])
def Index2():
    image = db.get_image()
    return render_template('imagedisplay.html',image=image)

@app.route('/edit', methods = ['POST', 'GET'])
def get_employee():
    if request.method == 'POST':
        print('----------------1111111111-----------------------------')
        #print(ID)
        print('----------------222222222222-----------------------------')
    return render_template('login.html')


@app.route('/delete', methods = ['POST','GET'])
def delete_employee():
    return redirect(url_for('Registration_information.html'))


@app.route('/seatviewpage')
def Indexseat():
     list_users = db.get_seat_details()
     #print(list_users)
     return render_template('seat_selectionpage.html', list_users = list_users)
 

@app.route('/update_seates', methods=['POST'])
def add_student():
    if request.method == 'POST':
       listup = request.form.getlist('mycheckbox')
       for i in listup:
           print(int(i))
           db.update_seat_by_id(int(i))
    return redirect(url_for("Indexseat"))
       



if __name__=="__main__":
    app.run(host='127.0.0.9',port=4455,debug=True) 