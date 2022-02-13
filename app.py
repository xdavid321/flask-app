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
def index():
    return render_template('login.html')



@app.route('/login',methods = ['POST','GET'])
def login():  
    if request.method == 'POST':
        email_html = request.form['email']
        password_html = request.form['password']
        User_details = db.get_email_password_details()
        for i in User_details:
               emails_temp = (i[0])
               password_temp = (i[1])
        if email_html == emails_temp and password_html == password_temp :
                print('success')
        return 'welcome'


@app.route('/signup')
def signup():
    return render_template('registration.html')






@app.route('/registration',methods = ['POST','GET'])
def registration():
    if request.method == 'POST':
        fName = request.form['fName']
        lName = request.form['lName']
        email = request.form['email']
        password = request.form['password']
        db.insert_details(fName, lName,email,password)
        details = db.get_details()
        print(details)

        '''for detail in details:
            var = detail
        return render_template('registration.html',var=var)
'''


if __name__ == "__main__":
    
    app.run(debug=True)