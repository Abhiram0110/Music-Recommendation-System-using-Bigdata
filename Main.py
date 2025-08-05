from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial
import subprocess
from playsound import playsound
import multiprocessing

def hadoopCommunication(args_list):
    print('Running system command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return =  proc.returncode
    return s_return, s_output, s_err  

dataset = pd.read_csv("Dataset/Dataset.csv")
names = dataset['Song_Details']

tfidf_vectorizer = TfidfVectorizer(use_idf=True, smooth_idf=False, norm=None, decode_error='replace')
tfidf = tfidf_vectorizer.fit_transform(dataset['Song_Details']).toarray()    

app = Flask(__name__)
app.secret_key = 'music'
global p

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', msg='')

@app.route('/Recommend', methods=['GET', 'POST'])
def Recommend():
    return render_template('Recommend.html', msg='')

@app.route('/StopPlaying', methods=['GET', 'POST'])
def StopPlaying():
    global p
    p.terminate()
    return render_template('Recommend.html', msg='')

@app.route('/PlaySong', methods=['GET', 'POST'])
def PlaySong():
    if request.method == 'GET':
        global p
        song_id = request.args.get("sid")
        print(song_id+"================")
        song_id = int(song_id)
        name = names[song_id]
        name = name.replace(" ","_")
        name = name+".wav"
        if os.path.exists("static/Download/"+name) == False:
            (ret, out, err)= hadoopCommunication(['C:\\hadoop\\bin\\hdfs.cmd', 'dfs', '-get', "hdfs://localhost:9000/Songs/Songs/"+name, "static/Download/"+name])
        p = multiprocessing.Process(target=playsound, args=('static/Download/'+name,))
        p.start()    
        return render_template('PlaySong.html', msg='Playing')

@app.route('/RecommendAction', methods=['GET', 'POST'])
def RecommendAction():
    if request.method == 'POST':
        data = request.form['t1']
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Liking Text</font></th>'
        output+='<th><font size=3 color=black>Recommended Song</font></th>'
        output+='<th><font size=3 color=black>Recommended Ranking</font></th>'
        output+='<th><font size=3 color=black>Play Song</font></th></tr>'
        input_text = [data]
        input_text = tfidf_vectorizer.transform(input_text).toarray()
        print(input_text)
        distances_list = list()
        for i in range(len(tfidf)):
            recommendation = 1 - spatial.distance.cosine(tfidf[i], input_text)
            distances_list.append((i, recommendation))
        distances_list.sort(key=lambda tuples: tuples[1], reverse = True)
        for i in range(len(distances_list)): #
            index = distances_list[i][0]
            similarity = distances_list[i][1]
            if similarity > 0:
                print(str(index)+" "+names[index]+" "+str(similarity))
                output+='<tr><td><font size=3 color=black>'+data+'</font></td>'
                output+='<td><font size=3 color=black>'+names[index]+'</font></td>'
                output+='<td><font size=3 color=black>'+str(similarity)+'</font></td>'
                output+='<td><a href=\'PlaySong?sid='+str(index)+'\'><font size=3 color=black>Click Here to Play Song</font></a></td></tr>'
        output += "</table><br/><br/><br/><br/><br/>"        
        return render_template('ViewRecommendation.html', msg=output)
    
if __name__ == '__main__':
    app.run()         
