import requests
import json
import datetime

from config import chave

# OK - TODO:Importar o dia atual e usa-lo como chave em uma variável
data_atual = datetime.datetime.today().date()



#TODO: Criar um arquivo de variáveis de ambiente e aplicar essas variáveis as urls
#TODO: Criar um arquivo de urls
time_daily_B3SA3= "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=B3SA3.SAO&interval=5min&apikey="+chave

symbol_search_B3SA3 = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=B3SA3&apikey="+chave

status_list = "https://www.alphavantage.co/query?function=LISTING_STATUS&state=delisted&&apikey="+chave



# r = requests.get(sla)
# r2 = requests.get(sla2)

#TODO: Descobrir como procurar os simbolos dentro do status_list
r3 = requests.get(status_list)

# jason = (json.loads(r.text))

# print(r2.text)
# print(jason["Time Series (Daily)"]["2021-05-14"])

print(r3.text)


#TODO: Fazer as conexões com o banco de dados
#TODO: Fazer a verificação através da data especificada
