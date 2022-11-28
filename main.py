from flask import Flask, render_template, request, redirect
import json 
import os
from backend import backend
import pathlib
from google.cloud import storage

def get_configuration(input):
    with open(input) as filestream:
        obj = json.load(filestream)
    return obj


app = Flask(__name__)
config = get_configuration(input = "config.json")
db = backend(config)
session = {}
backup_path = 'storage_files'

@app.route('/')
def base_page():
    return(redirect(f'{base_url}/login'))

@app.route("/")
def login():
     if request.method == 'POST':
        print(request.form)
        if request.form['sigin'] == "Login":
            eml = request.form.get('email')
            pwd = request.form.get('password')
            cmd = f"select * from accounts  where email='{eml}' and password='{pwd}'"
            df = db.det_get(cmmd=cmd)
            print("Login method invoked")
            if len(df) != 0:
                session['session'] = {
                    'user': df['username'].values[0], "email": df['email'].values[0]}
                return redirect(f'{base_url}/share')
                return render_template('login.html')
                return render_template("login.html", title="HOME PAGE")

@app.route("/register")
def register():
    print("Login method invoked")
    if request.method == 'POST':
        if request.form['signup'] == "Register":
            user = request.form.get('username')
            print(user)
            email = request.form.get('new_email')
            pass_ = request.form.get('new_password')
            rep_pass = request.form.get('new_rep_password')
            exist_cmd = f"select id from accounts where email='{email}'"
            exist_account = db.det_get(cmmd=exist_cmd)
            if ((pass_ == rep_pass)):
                insert_account = [
                    {"email": email, "username": user, "password": pass_}]
                db.put_dt(table_name="accounts",
                          json_data=insert_account)
                return redirect(f'{base_url}/login')
    return render_template("register.html", title="register page")

@app.route('/register/<id>', methods=['POST', 'GET'])
def register_pages(id):
    print("Login method invoked")
    args = request.args
    name = args.get('id')
    exist_cmd = f"select * from accounts where email='{id}'"
    exist_account = db.det_get(cmmd=exist_cmd).values.tolist()
    xist_account = exist_account[0]
    print((exist_account))
    return render_template('register.html',username=exist_account[1],email=exist_account[2])

@app.route("/share")
def share():
 
 return render_template("share.html", title="share page")


host = config['dev_ip']
base = "127.0.0.1"
port = config['port']
base_url = f"http://{base}:{port}"

if __name__ == "__main__":
    app.run(debug=True)

