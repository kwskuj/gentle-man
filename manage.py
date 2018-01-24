from flask import Flask,render_template,jsonify
import psycopg2
import json
import cv2 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/all_video")
def render_allvideo():
   
    return render_template("all_video.html")

# @app.route("/test")
# def db_test():
#     connnection = psycopg2.connnect("host=localhost port=5432 dbname=postgres" user=kawsakiyuji)
#     connnection.get_backend_pid()

if __name__ == '__main__':
   app.run(debug = True)