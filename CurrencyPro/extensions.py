from config import keys
import requests
import json

class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amoute: str):

        if quote == base:
            raise ConvertionExeption(f'Вы запросили одинаковую валюту {base}')

        if keys.get(quote) == None or keys.get(base) == None:
            raise ConvertionExeption('Вы указали несуществующую валюту в списке')

        try:
            amoute = float(amoute)
        except ValueError:
            raise ConvertionExeption('Укажите верное количество валюты')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/c691f5ab0a12fd8d38290844/latest/{quote}')
        total = json.loads(r.content).get('conversion_rates').get(base)

        return total