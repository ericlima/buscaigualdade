# importing the requests library 
import requests 

# api-endpoint 
URL = "https://dre.pt/web/guest/home/-/dre/calendar/normal/I?day=2020-03-04" #&date=2020-03-01"

# location given here 
location = "dre.pt"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

# Documento em formato PDF
# href="/application/conteudo/

pos = r.content.decode("utf-8").find("/application/conteudo/")

print(pos)

