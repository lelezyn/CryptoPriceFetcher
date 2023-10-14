import requests

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data[crypto_id]['usd']
        return price
    else:
        return None

crypto_id = "bitcoin"  # Pode substituir por qualquer outra criptomoeda suportada pelo CoinGecko
price = get_crypto_price(crypto_id)

if price:
    print(f"O preço atual do {crypto_id} é: ${price}")
else:
    print("Não foi possível obter o preço da criptomoeda.")
