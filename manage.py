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
      

@app.route("/test",methods=['GET'])
def ajax_test():
    
    connection = psycopg2.connect(
      database ='postgres',
      user ='kawasakiyuji',
      host = 'localhost',
      port = 5432
      )
    
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM videos')
    
    test_data = cursor.fetchall()
    cursor.close()
    
    for row in test_data:
        print(row)
    
    return json.dumps(test_data)

if __name__ == '__main__':
    app.run(debug=True)