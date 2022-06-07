import requests

class cambio(object):

    def conv(coin):
        coin = coin.upper()
        url = f'http://economia.awesomeapi.com.br/json/last/{coin}-BRL'
        api_r = requests.get(url).json()[coin+'BRL']['bid']
        
        return api_r
