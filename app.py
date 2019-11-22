from flask import Flask, redirect, url_for, request, render_template
from malkennsla import finnaOrd, correct, nafnord, greiningarstr, no_beyging #, sagnord, lysingarord, 
import csv

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/no')
def no():
    ordid = finnaOrd()
    no = nafnord(ordid)
    rett_svar = no_beyging(no)
    print("HALLOHALLOHALLO HALLO ", rett_svar)
    print("ÞAÐ SEM GREININGARSTR FÆR INN: ", rett_svar, 'no')
    setning = greiningarstr(rett_svar[1], 'no')
    print('SETNING YOYOYOYOO SKRKSKRKRSKRKRS: ', setning)
    return render_template('noun.html', nafno = no, sent = setning)

@app.route('/submit', methods=["POST"])
def noun():
    #sv = question()
    ordid = finnaOrd()
    no = nafnord(ordid)
    rett_svar = no_beyging(no)
    setning = greiningarstr(rett_svar[1], 'no')
    print('SETNING YOYOYOYOO: ', setning)
    answer = request.form['answer']
    if (correct(rett_svar[0], answer)):
        x = "Rétt svar"
    else:
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


# @app.route('/so')
# def verb():
#     q = question()
#     return render_template('verb.html', question = q)


# @app.route('/lo')
# def adj():
#     q = question()
#     return render_template('adj.html', question = q)

if __name__ == '__main__':
   app.run(debug = True)