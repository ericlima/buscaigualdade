# importing the requests library 
import requests 

import urllib.request as urllib2

import datetime

import os

import sys

def download_file(url):
    try:
        elements = url.split("/")
        pdf_file = urllib2.urlopen(url)
        with open(DOWNLOADS + elements[-1]+'.pdf','wb') as output:
            output.write(pdf_file.read())
        return elements[-1]
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return ""

inicio = datetime.date.today() - datetime.timedelta(days=30)
fim = datetime.date.today()

print("Inicio:",inicio)
print("fim:",fim)

numdays = 30

base = datetime.date.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]

# api-endpoint 
URL = "https://dre.pt/web/guest/home/-/dre/calendar/normal/II?day=" #2020-03-06&date=2020-03-01"

DOWNLOADS = 'Downloads/'

# location given here 
location = "dre.pt"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 

for d in date_list:
    url2 = URL + d.isoformat()
    #print(url2)

    # sending get request and saving the response as response object 
    r = requests.get(url = url2, params = PARAMS) 

    # Documento em formato PDF
    # href="/application/conteudo/

    pos1 = r.content.decode("utf-8").find("/application/conteudo/")
    referencia = r.content.decode("utf-8")[pos1:]

    pos2 = referencia.find(" title")-1

    link = "https://dre.pt"+referencia[:pos2]

    arq = download_file(link)

    if (len(arq)>1):
        print(arq)
        text = os.popen("pdftotext {}".format(DOWNLOADS + arq + '.pdf')).read()
        with open(DOWNLOADS + arq + '.txt') as f:
            if 'Porto Seguro' in f.read():
                print("porto seguro = true")

    #print(text)
