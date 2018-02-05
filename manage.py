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
      

@app.route("/new_video",methods=['GET'])
def new_video():
    
    connection = psycopg2.connect(
      database ='postgres',
      user ='kawasakiyuji',
      host = 'localhost',
      port = 5432
      )
    
    cursor = connection.cursor()
    cursor.execute('SELECT new_video FROM videos')
    
    new_data = cursor.fetchall()
    cursor.close()
    for i in new_data:
        print(i)
    return json.dumps(new_data)

@app.route("/recommend",methods=['GET'])
def recommend():
    
    connection = psycopg2.connect(
      database ='postgres',
      user ='kawasakiyuji',
      host = 'localhost',
      port = 5432
      )
    
    cursor = connection.cursor()
    cursor.execute('SELECT recommend FROM videos')
    
    recommend_data = cursor.fetchall()
    cursor.close()

    for i in recommend_data:
        print(i)

    return json.dumps(recommend_data)

@app.route("/rank",methods=['GET'])
def rank():
    
    connection = psycopg2.connect(
      database ='postgres',
      user ='kawasakiyuji',
      host = 'localhost',
      port = 5432
      )
    
    cursor = connection.cursor()
    cursor.execute('SELECT rank FROM videos')
    
    rank_data = cursor.fetchall()
    cursor.close()

    for i in rank_data:
        print(i)

    return json.dumps(rank_data)

@app.route("/recently",methods=['GET'])
def recently():
    
    connection = psycopg2.connect(
      database ='postgres',
      user ='kawasakiyuji',
      host = 'localhost',
      port = 5432
      )
    
    cursor = connection.cursor()
    cursor.execute('SELECT recently FROM videos')
    
    recently_data = cursor.fetchall()
    cursor.close()

    for i in recently_data:
        print(i)

    return json.dumps(recently_data)

if __name__ == '__main__':
    app.run(debug=True)