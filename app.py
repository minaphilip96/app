from flask import Flask, render_template, request, jsonify, redirect, url_for
import json


app = Flask(__name__)
file=open("database.json","r")
data = json.load(file)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/all_entry")
def all_entry():
    return render_template("all_entry.html",entry=data)

@app.route("/new_entry",methods=["POST","GET"])
def new_entry():
    if request.method=="GET":
        return render_template("new_entry.html")
    else:
            one=request.form.get("msg")
            data.append(one)
            with open("database.json","w")as out:
                 json.dump(data,out)
            return redirect("/")

@app.route("/personal")
def me():
     return render_template("personal.html")          
app.run()