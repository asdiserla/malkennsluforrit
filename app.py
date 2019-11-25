from flask import Flask, redirect, url_for, request, render_template
from malkennsla import findWord, rett_rangt, nafnord, greiningarstr, ord_beyging, saekja_rett
import csv
import re

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/no')
def no():
    ordid = findWord('no')
    no = nafnord('no', ordid)
    rett_svar = ord_beyging(no, 'no')
    setning = greiningarstr(rett_svar[1], 'no')
    grstrengur = rett_svar[1]
    return render_template('game.html', nafno = no, sent = setning, grstrr = grstrengur, ordfl = 'no')

@app.route('/so')
def so():
    ordid = findWord('so')
    so = nafnord('so', ordid)
    rett_svar = ord_beyging(so, 'so')
    setning = greiningarstr(rett_svar[1], 'so')
    grstrengur = rett_svar[1]
    return render_template('game.html', sagno = so, sent = setning, grstrr = grstrengur, ordfl = 'so')

@app.route('/lo')
def lo():
    ordid = findWord('lo')
    lo = nafnord('lo', ordid)
    rett_svar = ord_beyging(lo, 'lo')
    setning = greiningarstr(rett_svar[1], 'lo')
    grstrengur = rett_svar[1]
    return render_template('game.html', lysingaro = lo, sent = setning, grstrr = grstrengur, ordfl = 'lo')

@app.route('/submit', methods=['POST'])
def noun():
    if request.method == 'POST':
        answer = request.form['answer'].lower()
        question = request.form['quest']

        gs = request.form['greiningarstrengurinn']
        if (re.search('/no', request.referrer)):
            correctAnswer = saekja_rett(question, gs, 'no')
        elif (re.search('/so', request.referrer)):
            correctAnswer = saekja_rett(question, gs, 'so')
        elif (re.search('/lo', request.referrer)):
            correctAnswer = saekja_rett(question, gs, 'lo')

        if (answer == correctAnswer):
            if (re.search('/no', request.referrer)):
                return render_template('feedback.html', correct = correctAnswer, ordfl = 'no', right = True)
            elif (re.search('/so', request.referrer)):
                return render_template('feedback.html', correct = correctAnswer, ordfl = 'so', right = True)
            elif (re.search('/lo', request.referrer)):
                return render_template('feedback.html', correct = correctAnswer, ordfl = 'lo', right = True)
        else:
            if (re.search('/no', request.referrer)):
                return render_template('feedback.html', correct = correctAnswer, ordfl = 'no', right = False)
            elif (re.search('/so', request.referrer)):
                return render_template('feedback.html', correct = correctAnswer, ordfl = 'so', right = False)
            elif (re.search('/lo', request.referrer)):
                return render_template('feedback.html', correct = correctAnswer, ordfl = 'lo', right = False)

if __name__ == '__main__':
   app.run(debug = True)