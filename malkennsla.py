import nltk
import csv
import random
import requests
import json

# nafnordalisti = ['EFET', 'EFETgr', 'EFFT', 'EFFTgr', 'NFET', 'NFETgr', 'NFFT', 'NFFTgr',
#            'ÞFET', 'ÞFETgr', 'ÞFFT', 'ÞFFTgr', 'ÞGFET', 'ÞGFETgr', 'ÞGFFT', 'ÞGFFTgr']

reglur_no = {'NF': 'nefnifalli', 'ÞF': 'þolfalli', 'ÞGF': 'þágufalli', 'EF': 'eignarfalli',
             'ET': 'eintölu', 'FT': 'fleirtölu', 'gr': 'með greini'}

reglur_so = {'GM': 'germynd,', 'VH': 'viðtengingarhætti,', 'NH': 'nafnhætti,', 'LHNT': 'lýsingarhætti nútíðar', 'LHÞT': 'lýsingarhætti þátíðar,',
             'FH': 'framsöguhætti,', 'BH': 'boðhætti', '1P': '1. persónu', '2P': '2. persónu', '3P': '3. persónu',
             'NF': 'nefnifalli', 'ÞF': 'þolfalli', 'ÞGF': 'þágufalli', 'EF': 'eignarfalli', 'FT': 'fleirtölu', 'ET': 'eintölu',
             'HK': 'hvorugkyni', 'KK': 'karlkyni', 'KVK': 'kvenkyni'}

reglur_lo = {'ESG': 'efsta stigi', 'EVB': 'efsta stigi', 'FSB': 'frumstigi', 'FVB': 'frumstigi',
             'MST': 'miðstigi', 'ET': 'eintölu', 'FT': 'fleirtölu', 'NF': 'nefnifalli', 'ÞF': 'þolfalli',
             'ÞGF': 'þágufalli', 'EF': 'eignarfalli', 'HK': 'hvorugkyni', 'KK': 'karlkyni', 'KVK': 'kvenkyni'}

# print("REGLUR: ", reglur_no.values())
with open("ordmyndalisti.txt") as words:
      wordlist = [x.rstrip() for x in words]

def finnaOrd():
  variable = random.choice(wordlist)
  return variable

# new_wordlist = [word for word in wordlist if word != variable]

# Nafnorð
def nafnord(variable):
  response = requests.get(
    "https://bin.arnastofnun.is/api/ord/no/{}".format(variable))

  while (type(response.json()) is not list):
    if (type(response.json()) is list):
        break
    variable = random.choice(wordlist)
    response = requests.get(
        "https://bin.arnastofnun.is/api/ord/no/{}".format(variable))

  print("RANDOM nafnorð ORÐIÐ ER: ", variable)
  rett_ord = response.json()[0]['bmyndir']
  ordid = rett_ord[0]['b']
  return ordid

# Sagnorð
def sagnord(variable):
  response = requests.get(
    "https://bin.arnastofnun.is/api/ord/so/{}".format(variable))

  while (type(response.json()) is not list):
    if (type(response.json()) is list):
        break
    variable = random.choice(wordlist)
    response = requests.get(
        "https://bin.arnastofnun.is/api/ord/so/{}".format(variable))

  print("RANDOM sagnorð ORÐIÐ ER: ", variable)
  rett_ord = response.json()[0]['bmyndir']
  ordid = rett_ord[0]['b']
  return ordid

# Lýsingarorð
def lysingarord(variable):
  response = requests.get(
    "https://bin.arnastofnun.is/api/ord/lo/{}".format(variable))

  while (type(response.json()) is not list):
    if (type(response.json()) is list):
        break
    variable = random.choice(wordlist)
    response = requests.get(
        "https://bin.arnastofnun.is/api/ord/lo/{}".format(variable))

  print("RANDOM lýsingarorð ORÐIÐ ER: ", variable)
  rett_ord = response.json()[0]['bmyndir']
  ordid = rett_ord[0]['b']
  return ordid

# Tekur inn greiningarstreng og skilar viðeigandi setningu
def greiningarstr(grst, ordfl):
    strengur = ''
    
    if ordfl == 'no':
      reglur = reglur_no
    elif ordfl == 'so':
      reglur = reglur_so
    elif ordfl == 'lo':
      reglur = reglur_lo

    x = len(reglur)
    for (key, value) in reglur.items():
      if key in grst:
        strengur += value + " "
        print("WHOOOOPPP", strengur)
    return strengur    

def ord_beyging(ordid, ordfl):
  print("FÆ INN: ", ordid)
  response = requests.get(
    "https://bin.arnastofnun.is/api/ord/{}".format(ordid))
  # Fjöldi beygingarmynda
  fjoldi_bm = len(response.json()[0]['bmyndir'])
  # Velja random beygingarmynd sem á að fallbeygja
  rand_bm = random.randint(0, fjoldi_bm - 1)
  beygingarmyndir = response.json()[0]['bmyndir']
  ord_bm = beygingarmyndir[rand_bm]['b'] # beygingarmynd
  ord_gs = beygingarmyndir[rand_bm]['g'] # greiningarstrengur

  print('RÉTT SVAR SKRRRRT: ', ord_bm, ord_gs)
  #TODO senda inn rétt no so eða lo
  greiningarstr(ord_gs, ordfl)
  return ord_bm, ord_gs

variable = finnaOrd()
no = nafnord(variable)
# rettasvarid = ord_beyging(no)


def rett_rangt(svar):
    if (svar == rettasvarid[0]):
        return True
    else:
        return False

# # print(spurning())

def correct(a, b):
  return a == b





# tags = []
# with open('tags.csv') as strengir:
#     for line in strengir:
#         line_words = line.strip().split(';')
#         if (len(line_words) == 5):
#             tags.append(line_words)

###########################
# new_wordlist = [word for word in wordlist if word != variable]

# response = requests.get(
#     "https://bin.arnastofnun.is/api/ord/{}".format(variable))

# data = response.json()

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
