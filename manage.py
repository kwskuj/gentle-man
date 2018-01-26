# coding: UTF-8
from flask import Flask,render_template,jsonify
import psycopg2
import json
import cv2 
import request

app = Flask(__name__)

@app.route("/")
def top():
    
    return render_template("top_page.html")

@app.route("/all_video")
def render_allvideo():
   
    return render_template("all_video.html")

@app.route("/test")
def ajax_test():
    return json.dumps({'1':[123],'2':[234],'3':[111]})

if __name__ == '__main__':
    app.run(debug=True)