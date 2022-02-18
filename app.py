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


@app.route('/')
def home():
    return render_template('homePage.html')
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



if __name__ == "__main__":
    
    app.run(debug=True)