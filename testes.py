import datetime

inicio = datetime.date.today() - datetime.timedelta(days=30)
fim = datetime.date.today()

print("Inicio:",inicio)
print("fim:",fim)

numdays = 30

base = datetime.date.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]

for d in date_list:
    print(d)
