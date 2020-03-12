# importing the requests library 
import requests 

import urllib.request as urllib2

import datetime

def download_file(url):
    elements = url.split("/")
    pdf_file = urllib2.urlopen(url)
    with open(elements[-1]+'.pdf','wb') as output:
        output.write(pdf_file.read())
    return

inicio = datetime.date.today() - datetime.timedelta(days=30)
fim = datetime.date.today()

print("Inicio:",inicio)
print("fim:",fim)

numdays = 30

base = datetime.date.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]

# api-endpoint 
URL = "https://dre.pt/web/guest/home/-/dre/calendar/normal/II?day=" #2020-03-06&date=2020-03-01"

# location given here 
location = "dre.pt"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 

for d in date_list:
    url2 = URL + d.isoformat()
    print(url2)

    # sending get request and saving the response as response object 
    r = requests.get(url = url2, params = PARAMS) 

    # Documento em formato PDF
    # href="/application/conteudo/

    pos1 = r.content.decode("utf-8").find("/application/conteudo/")
    referencia = r.content.decode("utf-8")[pos1:]

    pos2 = referencia.find(" title")-1

    link = "https://dre.pt"+referencia[:pos2]

    download_file(link)


