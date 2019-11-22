import nltk
import csv
import random
import requests
import json

nafnordalisti = ['EFET', 'EFETgr', 'EFFT', 'EFFTgr', 'NFET', 'NFETgr', 'NFFT', 'NFFTgr',
           'ÞFET', 'ÞFETgr', 'ÞFFT', 'ÞFFTgr', 'ÞGFET', 'ÞGFETgr', 'ÞGFFT', 'ÞGFFTgr']

reglur_no = {'NF': 'nefnifalli', 'ÞF': 'þolfalli', 'ÞGF': 'þágufalli', 'EF': 'eignarfalli',
             'ET': 'eintölu', 'FT': 'fleirtölu', 'gr': 'með greini'}

# print("REGLUR: ", reglur_no.values())
with open("ordmyndalisti.txt") as words:
      wordlist = [x.rstrip() for x in words]

def finnaOrd():
  variable = random.choice(wordlist)
  return variable

# new_wordlist = [word for word in wordlist if word != variable]

def nafnord(variable):
  response = requests.get(
    "https://bin.arnastofnun.is/api/ord/no/{}".format(variable))
  print('RESPONSESSESESE: ', response)

  while (type(response.json()) is not list):
    if (type(response.json()) is list):
        break
    variable = random.choice(wordlist)
    response = requests.get(
        "https://bin.arnastofnun.is/api/ord/no/{}".format(variable))
    # new_wordlist = [word for word in wordlist if word != variable]


  print("RANDOM ORÐIÐ ER: ", variable)

  rett_ord = response.json()[0]['bmyndir']
  ordid = rett_ord[0]['b']
  stofn = response.json()[0]['ord']
  # print('STOFN ORÐSINS: ', stofn)
  # print('orðið sjálft: ', ordid)
  greiningarstrengur = rett_ord[0]['g']
  # print('greiningarstrengur: ', greiningarstrengur)
  return ordid

# Tekur inn greiningarstreng og skilar viðeigandi setningu
def greiningarstr(grst, ordfl):
    strengur = ''
    if ordfl == 'no':
      x = len(reglur_no)
      for (key, value) in reglur_no.items():
        if key in grst:
          strengur += value + " "
          print("WHOOOOPPP", strengur)
    return strengur    

# Finna greiningarstreng
# def finnaGrs(no):
#     response = requests.get(
#       "https://bin.arnastofnun.is/api/ord/{}".format(no))

def no_beyging(no):
  print("FÆ INN: ", no)
  response = requests.get(
    "https://bin.arnastofnun.is/api/ord/{}".format(no))
  # Fjöldi beygingarmynda
  fjoldi_bm = len(response.json()[0]['bmyndir'])
  # Velja random beygingarmynd sem á að fallbeygja
  rand_bm = random.randint(0, fjoldi_bm - 1)
  beygingarmyndir = response.json()[0]['bmyndir']
  ord_bm = beygingarmyndir[rand_bm]['b'] # beygingarmynd
  ord_gs = beygingarmyndir[rand_bm]['g'] # greiningarstrengur

  print('RÉTT SVAR SKRRRRT: ', ord_bm, ord_gs)
  greiningarstr(ord_gs, 'no')
  # print("SUBSTRING: ", next(bm in ord_gs for bm in nafnordalisti))
  return ord_bm, ord_gs
#  print(response.json()[0]['bmyndir'])
# print("FJÖLDI BEYGINGARMYNDA ", len(response.json()[0]['bmyndir']))

variable = finnaOrd()
no = nafnord(variable)
print(no_beyging(no))

tags = []
with open('tags.csv') as strengir:
    for line in strengir:
        line_words = line.strip().split(';')
        if (len(line_words) == 5):
            tags.append(line_words)

###########################
# new_wordlist = [word for word in wordlist if word != variable]

# response = requests.get(
#     "https://bin.arnastofnun.is/api/ord/{}".format(variable))

# data = response.json()

# if (type(data) is list):  # == "<class 'list'>"
#     print("RANDOM ORÐIÐ ER: ", variable)

# # TODO getur gerst að orð hafi ekki bmyndir
# while (type(response.json()) is not list):
#     if (type(response.json()) is list):
#         break
#     variable = random.choice(new_wordlist)
#     response = requests.get(
#         "https://bin.arnastofnun.is/api/ord/{}".format(variable))
#     new_wordlist = [word for word in wordlist if word != variable]
###########################

# print("RANDOM ORÐIÐ ER: ", variable)

# rett_ord = response.json()[0]['bmyndir']
# ordid = rett_ord[0]['b']
# stofn = response.json()[0]['ord']
# print('STOFN ORÐSINS: ', stofn)
# print('orðið sjálft: ', ordid)
# greiningarstrengur = rett_ord[0]['g']
# print('greiningarstrengur: ', greiningarstrengur)


#*
# blabla = [c for (a, b, c, d, e) in tags if b == greiningarstrengur]
# print('blabla: ', blabla)
# beygingarmynd = blabla[0]

# def question():
#     if (variable == no):
#         x = "Hver er stofn orðsins '{}'? ".format(variable)
#     else:
#         x = "Beygðu %s í %s? " % (variable, beygingarmynd)
#     return x

# def rett_rangt(svar):
#     if (svar == stofn):
#         return True
#     else:
#         return False

# # print(spurning())

def correct(a, b):
  return a == b
