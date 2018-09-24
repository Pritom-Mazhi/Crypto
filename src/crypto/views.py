from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json

    #grab crypto price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=BDT")
    price = json.loads(price_request.content.decode('utf-8'))

    #grab crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content.decode('utf-8'))
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST["quote"]
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=BDT")
        crypto = json.loads(crypto_request.content.decode('utf-8'))
        return render(request, 'prices.html', {'quote' : quote, 'crypto' : crypto})

    else:
        notfound = "Please enter a correct crypto currency symbol in the search box above, if two then separate them with a comma and avoid a space after comma...."
        return render(request, 'prices.html', {'notfound': notfound})
