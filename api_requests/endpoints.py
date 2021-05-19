import requests
import json

KEY = "6NLEKEA6FR9NAY0W"


#OK - TODO: Criar um arquivo de variáveis de ambiente e aplicar essas variáveis as urls
#OK - TODO: Criar um arquivo de urls

def symbol_search(SYMBOL):
    '''
    Respossavel palas requisições ao endpoint symbol_search da API
    :return: dicionário com o body da requisição 
    '''

    symbol_search = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords="+SYMBOL+"&apikey="+KEY
    return json.loads(requests.get(symbol_search).text)
    


def time_daily(SYMBOL):
    '''
    Respossavel palas requisições ao endpoint time_daily da API
    :return: dicionário com o body da requisição 
    '''

    time_daily= "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+SYMBOL+"&interval=5min&apikey="+KEY
    return json.loads(requests.get(time_daily).text)
    
