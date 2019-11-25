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


# Náum í orðin í orðmyndalistanum og setjum þau í fylki
with open("ordmyndalisti.txt") as words:
      wordlist = [x.rstrip() for x in words]


# Naíum í random orð úr listanum
def findWord(ordfl):
    variable = random.choice(wordlist)
    return variable


# Tekur inn orð ásamt orðflokkinum sem orðið er í
# Ef orðið er ekki í APA-num (https://bin.arnastofnun.is/api/) eða
#   orðið hefur engar beygingarmyndir skráðar í honum leitum við að 
#   nýju og nýju orði þar til við finnum orð sem uppfyllir þessi tvö skilyrði
def wordThatFits(ordfl, variable):
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


# Tekur inn orð og orðflokknum sem orðið er í og skilar beygingunni
#   á orðinu sem notandi á að giska á
def ord_beyging(ordid, ordfl):
  response = requests.get(
    "https://bin.arnastofnun.is/api/ord/{}/{}".format(ordfl, ordid))

  # Fjöldi beygingarmynda
  fjoldi_bm = len(response.json()[0]['bmyndir'])

  # Velja random beygingarmynd sem notandi á að fallbeygja orðið í
  rand_bm = random.randint(0, fjoldi_bm - 1)

  # Finna allar beygingarmyndir orðsins
  beygingarmyndir = response.json()[0]['bmyndir']
  ord_bm = beygingarmyndir[rand_bm]['b']   # Random beygingarmyndin
  ord_gs = beygingarmyndir[rand_bm]['g']   # Random greiningarstrengurinn

  return ord_bm, ord_gs

# Sækir réttu beyginguna á orðinu sem notandinn á að beygja
def saekja_rett(ordid, grst, ordfl):
    response = requests.get(
      "https://bin.arnastofnun.is/api/ord/{}/{}".format(ordfl, ordid))
    
    beygingarmyndir = response.json()[0]['bmyndir']
    for i in range(len(beygingarmyndir)):
      if (beygingarmyndir[i]['g'] == grst):
        rett = beygingarmyndir[i]['b']
    return rett