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

# @app.route("/DBtest")
# def db_get():
      

@app.route("/test")
def ajax_test():
    return json.dumps({
  "players": [
    {
      "id": "0001",
      "name": "Nishikawa Haruki",
      "position": "center fielder"
    },
    {
      "id": "0002",
      "name": "Matsumoto Go",
      "position": "right fielder"
    },
    {
      "id": "0003",
      "name": "Brandon J. Laird",
      "position": "third baseman"
    } ,
    {
      "id": "0004",
      "name": "Nakata Sho",
      "position": "first baseman"
    }
  ]
})

if __name__ == '__main__':
    app.run(debug=True)