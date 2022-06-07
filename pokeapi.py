import requests
from exchange import cambio

class pokecambio(object):

    def gurl(camb):
        url = 'https://pokeapi.co/api/v2/pokemon/'
        value = cambio.conv(camb)
        str_value = ''
        if '.' in str(value):
            str_value = str(value).replace('.','')
            if str_value[0] == '0':
                str_value = str_value.replace('0', '')
            str_value = str_value[:3]
        api_r = requests.get(url + str_value)
        
        return api_r

    def ExcToPkm_name(camb):
        name = pokecambio.gurl(camb).json()['name']
        return name

    def ExcToPkm_img(camb):
        img = pokecambio.gurl(camb).json()['sprites']['other']['official-artwork']['front_default']
        return img

    def ExcToPkm_cambio(camb):
        value = cambio.conv(camb)
        return value

    def ExcToPkm_coins(camb):
        return 'BRL - ' + camb
