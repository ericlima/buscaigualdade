# importing the requests library 
import requests 
import urllib.request as urllib2
import datetime
import os
import os.path
import sys

def download_file(url):
    try:
        elements = url.split("/")
        pdf_file = urllib2.urlopen(url)
        pdf_path = DOWNLOADS + elements[-1]+'.pdf'
        if not os.path.exists(pdf_path):
            with open(pdf_path,'wb') as output:
                output.write(pdf_file.read())
        return elements[-1]
    except:
        print("error:", sys.exc_info()[0], ' = ', url)
        return ""

TEXT_TO_SEARCH = "Estatuto de Igualdade de Direitos e Deveres"

numdays = 180

inicio = datetime.date.today() - datetime.timedelta(days=numdays)
fim = datetime.date.today()

print("Inicio:",inicio)
print("fim:",fim)

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
        pdf_path = DOWNLOADS + arq + '.pdf'
        txt_path = DOWNLOADS + arq + '.txt'
        if not os.path.exists(txt_path): 
            os.popen("pdftotext {}".format(pdf_path)).read()

        if os.path.exists(txt_path):
            with open(txt_path) as f:
                if TEXT_TO_SEARCH in f.read():
                    print(TEXT_TO_SEARCH +" = true")

    #print(text)
