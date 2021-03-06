from flask import render_template
from app import app, mail
from flask import Flask, request,flash
from form import formx
from flask.ext.mail import Message
import os
from threading import Thread

def send_async_email(msg):
	mail.send(msg)

def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = text_body
    thr=Thread(target = send_async_email, args=[msg])
    thr.start()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = formx()
    if request.method== 'POST':
        subject=form.subject.data
        message=form.name.data+' said '+form.message.data+" form "+form.email.data
        send_email(subject,'form.email.data',['kiriko.brindley@gmail.com'],message)
    return render_template('index.html',form=form)

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});

@app.route('/projects', methods=['GET'])
def projects():
    print 'projects'
    return render_template('projects.html')

@app.route('/references', methods=['get'])
def references():
    print 'references'
    return render_template('references.html')

@app.route('/photography', methods=['GET'])
def photography():
    print 'photography'
    return render_template('photography.html')