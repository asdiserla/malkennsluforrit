import random
import requests
import json

reglur_no = {'NF': 'nefnifalli', 'ÞF': 'þolfalli', 'ÞGF': 'þágufalli', 'EF': 'eignarfalli',
             'ET': 'eintölu', 'FT': 'fleirtölu', 'gr': 'með greini'}

reglur_so = {'GM': 'germynd,', 'MM': 'miðmynd,', 'VH': 'viðtengingarhætti,', 'NH': 'nafnhætti,', 'LHNT': 'lýsingarhætti nútíðar', 'LHÞT': 'lýsingarhætti þátíðar,',
             'FH': 'framsöguhætti,', 'BH': 'boðhætti', '1P': '1. persónu', '2P': '2. persónu', '3P': '3. persónu',
             'NF': 'nefnifalli', 'ÞF': 'þolfalli', 'ÞGF': 'þágufalli', 'EF': 'eignarfalli', 'FT': 'fleirtölu', 'ET': 'eintölu',
             'HK': 'hvorugkyni', 'KK': 'karlkyni', 'KVK': 'kvenkyni', 'SAGNB': 'sagnbót'}

reglur_lo = {'ESG': 'efsta stigi', 'EVB': 'efsta stigi', 'FSB': 'frumstigi', 'FVB': 'frumstigi',
             'MST': 'miðstigi', 'ET': 'eintölu', 'FT': 'fleirtölu', 'NF': 'nefnifalli', 'ÞF': 'þolfalli',
             'ÞGF': 'þágufalli', 'EF': 'eignarfalli', 'HK': 'hvorugkyni', 'KK': 'karlkyni', 'KVK': 'kvenkyni'}

with open("ordmyndalisti.txt") as words:
      wordlist = [x.rstrip() for x in words]

with open("sagnord.txt") as words:
      verblist = [x.rstrip() for x in words]

def findWord(ordfl):
  if (ordfl == 'so'):
    variable = random.choice(verblist)
  else:
    variable = random.choice(wordlist)
  return variable

# Tekur inn orð ásamt orðflokkinum sem orðið er í
# Ef orðið er ekki í APA-num (https://bin.arnastofnun.is/api/) eða
# orðið hefur engar beygingarmyndir skráðar í honum leitum við að 
# nýju og nýju orði þar til við finnum orð sem uppfyllir þessi tvö skilyrði
def nafnord(ordfl, variable):
  response = requests.get(
    "https://bin.arnastofnun.is/api/ord/{}/{}".format(ordfl, variable))

  while (True):
    if (type(response.json()) is list and
          'bmyndir' in response.json()[0]):
        break
    variable = random.choice(wordlist)
    response = requests.get(
        "https://bin.arnastofnun.is/api/ord/{}/{}".format(ordfl, variable))

  print("RANDOM nafnorð ORÐIÐ ER: ", variable)
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
    return strengur    

def ord_beyging(ordid, ordfl):
  print("FÆ INN: ", ordid)
  response = requests.get(
    "https://bin.arnastofnun.is/api/ord/{}/{}".format(ordfl, ordid))
  # Fjöldi beygingarmynda
  fjoldi_bm = len(response.json()[0]['bmyndir'])
  # Velja random beygingarmynd sem á að fallbeygja
  rand_bm = random.randint(0, fjoldi_bm - 1)
  beygingarmyndir = response.json()[0]['bmyndir']
  ord_bm = beygingarmyndir[rand_bm]['b'] # beygingarmynd
  ord_gs = beygingarmyndir[rand_bm]['g'] # greiningarstrengur

  print('RÉTT SVAR SKRRRRT: ', ord_bm, ord_gs)
  greiningarstr(ord_gs, ordfl)
  return ord_bm, ord_gs


def saekja_rett(ordid, grst, ordfl):
    print("FÆ INN I SÆKJA RÉTT: ", ordid, grst)
    response = requests.get(
      "https://bin.arnastofnun.is/api/ord/{}/{}".format(ordfl, ordid))
    # if ('bmyndir' not in response.json()[0]):
    #     print("BEYGINGARMYNDIR ERU AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    beygingarmyndir = response.json()[0]['bmyndir']
    for i in range(len(beygingarmyndir)):
      if (beygingarmyndir[i]['g'] == grst):
        rett = beygingarmyndir[i]['b']
    return rett


def rett_rangt(svar):
    if (svar == rettasvarid[0]): #TODO setja i breytu
        return True
    else:
        return False