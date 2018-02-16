# coding: UTF-8
from flask import Flask,render_template,jsonify,request
import psycopg2
import json
import cv2 
import cgi

app = Flask(__name__)

def get_connection():
    connection = psycopg2.connect(
        database ='postgres',
        user ='kawasakiyuji',
        host = 'localhost',
        port = 5432
    )
    return connection

@app.route("/")
def top():
    
    return render_template("top_page.html")

@app.route("/all_video")
def render_allvideo():
   
    return render_template("all_video.html")

@app.route("/maintenance",methods=['GET'])
def maintenance():
    
    return render_template("maintenance.html")

@app.route("/new_video",methods=['GET'])
def new_video():   
   with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT video,videoimage,title FROM new_video_table');
        new_data = cur.fetchall()
        cur.close()

    return json.dumps(new_data)

@app.route("/recommend",methods=['GET'])
def recommend():
    with get_connection() as conn:
     with conn.cursor() as cur:
        cur.execute('SELECT video,videoimage,title FROM recommend_video_table');
        recommend_data = cur.fetchall()
        cur.close()

    return json.dumps(recommend_data)

@app.route("/rank",methods=['GET'])
def rank(): 
    with get_connection() as conn:
     with conn.cursor() as cur:
        cur.execute('SELECT video,videoimage,title FROM rank_video_table');
        rank_data = cur.fetchall()
        cur.close()

    return json.dumps(rank_data)

@app.route("/recently",methods=['GET'])
def recently():  
    with get_connection() as conn:
     with conn.cursor() as cur:
        cur.execute('SELECT video,videoimage,title FROM recently_video_table');
        recently_data = cur.fetchall()
        cur.close()

    return json.dumps(recently_data)

@app.route("/new_video_insert",methods=['POST'])
def new_video_insert():
    url = request.form['new_video_url']
    image = request.form['new_video_image']
    title = request.form['new_video_title']
    actor = request.form['new_video_actor']
    country = request.form['new_video_country']
    playtime= request.form['new_video_PlayTime']
    daytime = request.form['new_video_DayTime']

    with get_connection() as conn:
     conn.autocommit = True
     with conn.cursor() as cur:
        cur.execute('SELECT id FROM new_video_table')
        new_video = cur.fetchall()
        id_num = len(new_video) + 1 
        cur.execute('INSERT INTO new_video_table (id,video,videoimage,title,actor,country,daytime,playtime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (id_num,url,image,title,actor,country,daytime,playtime,))
        cur.execute('SELECT id FROM new_video_table')
        new_video = cur.fetchall()
        cur.close()

        return render_template("maintenance.html")

@app.route("/recommend_video_insert",methods=['POST'])
def recommend_video_insert():
    url = request.form['recommend_video_url']
    image = request.form['recommend_video_image']
    title = request.form['recommend_video_title']
    actor = request.form['recommend_video_actor']
    country = request.form['recommend_video_country']
    playtime= request.form['recommend_video_DayTime']
    daytime = request.form['recommend_video_PlayData']

    with get_connection() as conn:
     conn.autocommit = True
     with conn.cursor() as cur:
        cur.execute('SELECT id FROM recommend_video_table')
        recommend_video = cur.fetchall()
        id_num = len(recommend_video) + 1 
        cur.execute('INSERT INTO recommend_video_table (id,video,videoimage,title,actor,country,daytime,playtime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (id_num,url,image,title,actor,country,daytime,playtime,))
        cur.execute('SELECT id FROM recommend_video_table')
        recommend_video = cur.fetchall()
        cur.close()

        return render_template("maintenance.html")

@app.route("/rank_video_insert",methods=['POST'])
def rank_video_insert():
    url = request.form['rank_video_url']
    image = request.form['rank_video_image']
    title = request.form['rank_video_title']
    actor = request.form['rank_video_actor']
    country = request.form['rank_video_country']
    playtime= request.form['rank_video_DayTime']
    daytime = request.form['rank_video_PlayData']

    with get_connection() as conn:
     conn.autocommit = True
     with conn.cursor() as cur:
        cur.execute('SELECT id FROM rank_video_table')
        recommend_video = cur.fetchall()
        id_num = len(recommend_video) + 1 
        cur.execute('INSERT INTO rank_video_table (id,video,videoimage,title,actor,country,daytime,playtime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (id_num,url,image,title,actor,country,daytime,playtime,))
        cur.execute('SELECT id FROM rank_video_table')
        rank_video = cur.fetchall()
        cur.close()

        return render_template("maintenance.html")

@app.route("/recently_video_insert",methods=['POST'])
def recently_video_insert():
    url = request.form['recently_video_url']
    image = request.form['recently_video_image']
    title = request.form['recently_video_title']
    actor = request.form['recently_video_actor']
    country = request.form['recently_video_country']
    playtime= request.form['recently_video_DayTime']
    daytime = request.form['recently_video_PlayData']

    with get_connection() as conn:
     conn.autocommit = True
     with conn.cursor() as cur:
        cur.execute('SELECT id FROM recently_video_table')
        recommend_video = cur.fetchall()
        id_num = len(recommend_video) + 1 
        cur.execute('INSERT INTO recently_video_table (id,video,videoimage,title,actor,country,daytime,playtime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (id_num,url,image,title,actor,country,daytime,playtime,))
        cur.execute('SELECT id FROM recently_video_table')
        recently_video = cur.fetchall()
        cur.close()

        return render_template("maintenance.html")


# @app.route("/server_test",methods=['GET'])
# def server_test():  

#     connection = psycopg2.connect(
#       database ='kawasaki',
#       user ='kawasaki',
#       host = 'gentolman.comv9pymbm1i.us-east-2.rds.amazonaws.com',
#       password = 'kawasaki',
#       port = 5432
#       )   

#     cursor = connection.cursor()
    
#     cursor.execute('SELECT * FROM server_test')  

#     test_data = cursor.fetchall()
#     cursor.close()
    
#     for i in test_data:
#         print (i)

#     return json.dumps(test_data)

if __name__ == '__main__':
    app.run(debug=True)