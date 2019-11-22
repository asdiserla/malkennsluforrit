from flask import Flask, redirect, url_for, request, render_template
from malkennsla import finnaOrd, rett_rangt, nafnord, greiningarstr, ord_beyging, sagnord, lysingarord
import csv

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/no')
def no():
    ordid = finnaOrd()
    no = nafnord(ordid)
    rett_svar = ord_beyging(no, 'no')
    setning = greiningarstr(rett_svar[1], 'no')
    return render_template('noun.html', nafno = no, sent = setning)

@app.route('/submit', methods=['POST'])
def noun():
    #sv = question()
    ordid = finnaOrd()
    no = nafnord(ordid)
    rett_svar = ord_beyging(no, 'no')
    rett = rett_svar[0]
    setning = greiningarstr(rett_svar[1], 'no')
    if request.method == 'POST':
        answer = request.form['answer']
        print("SVARIÐ: ", answer, rett)
        if (rett == answer):
            print("RÉTT SVAR BBY")
            x = "Rétt svar"
        else:
            print("RANGT SVAR BBY")
            x = "Rangt svar"
        return render_template('noun.html', nafno = no, rettsvar = x, sent = setning)

# @app.route('/submit', methods=["POST"])
# def noun_answer():
#     q = question()
#     no = nafnord()
#     svar = request.form['answer']
#     if (rett_rangt(svar)):
#         print("RÉTT SVAR BITCH")
#         x = "Rétt svar"
#     else:
#         x = "Rangt svar"
#     return render_template('noun.html', question = q, correct = x)

@app.route('/so')
def so():
    ordid = finnaOrd()
    so = sagnord(ordid)
    rett_svar = ord_beyging(so, 'so')
    setning = greiningarstr(rett_svar[1], 'so')
    return render_template('verb.html', sagno = so, sent = setning)

#TODO laga, fæ nafnorð ef ég submita á /so
@app.route('/submit', methods=['POST'])
def verb():
    #sv = question()
    ordid = finnaOrd()
    so = sagnord(ordid)
    rett_svar = ord_beyging(so, 'so')
    rett = rett_svar[0]
    setning = greiningarstr(rett_svar[1], 'so')
    if request.method == 'POST':
        answer = request.form['answer']
        print("SVARIÐ: ", answer, rett)
        if (rett == answer):
            print("RÉTT SVAR BBY")
            x = "Rétt svar"
        else:
            print("RANGT SVAR BBY")
            x = "Rangt svar"
        return render_template('verb.html', sagno = so, rettsvar = x, sent = setning)

@app.route('/lo')
def lo():
    ordid = finnaOrd()
    lo = lysingarord(ordid)
    rett_svar = ord_beyging(lo, 'lo')
    setning = greiningarstr(rett_svar[1], 'lo')
    return render_template('adj.html', lysingaro = lo, sent = setning)

if __name__ == '__main__':
   app.run(debug = True)