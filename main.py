import requests

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data.get(crypto_id, {}).get('usd')
        if price is not None:
            return price
        else:
            return f"Criptomoeda '{crypto_id}' não encontrada."
    else:
        return f"Erro na requisição: {response.status_code}"

def main():
    crypto_id = input("Digite o ID da criptomoeda: ")
    price = get_crypto_price(crypto_id)

    if isinstance(price, str):
        print(price)
    else:
        print(f"O preço atual do {crypto_id} é: ${price}")


main()
    

    