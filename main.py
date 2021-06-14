from datetime import datetime, timedelta

from api_requests.endpoints import time_daily, symbol_search
from database.models import verify_register
from amb_var import TABLES


def verify_data(data_i, dias):
    """Recebe uma data e um número de dias e faz a subtração entre os
    dois
    :return:  datatime.date resultado
    """

    # Formata a data recebida em datatime.date
    data_i = datetime.strptime(data_i, "%Y-%m-%d").date()

    # Subtrai os dias da data
    data = data_i - timedelta(days=dias)
    return data


def init():
    for sy in TABLES:

        # Pegado as respostas dos endpoints selecionados
        dict_td = time_daily(sy)
        dict_ss = symbol_search(sy)

        # Usa os dados de 7 dias antes do ultimo Refresh da Api
        last_refreshed = dict_td["Meta Data"]["3. Last Refreshed"]
        dias = 7
        while dias != 0:
            data = verify_data(last_refreshed, dias)

            # Faz a verificação de status através do KeyError
            try:
                fechamento = dict_td["Time Series (Daily)"][str(data)]["4. close"]
                ativo = dict_td["Time Series (Daily)"][str(data)]["5. volume"]
                nome = dict_ss["bestMatches"][0]["2. name"]
                symbol = dict_ss["bestMatches"][0]["1. symbol"]
                status = True
                dados = {
                    "status": status,
                    "symbol": symbol,
                    "nome": nome,
                    "data": str(data),
                    "ativo": ativo,
                    "preco": fechamento,
                }

                # Envia os dados para serem validados e registrados
                resposta, msg = verify_register(dados)
                print(
                    f" * {data} - {symbol}",
                    msg,
                )

            except KeyError:
                print(f" * {data} - {sy} desabilitado")

            # Contador de dias
            dias -= 1


if __name__ == "__main__":
    init()
