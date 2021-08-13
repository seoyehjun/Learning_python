import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
print(btc)

fluctuation = btc['max_price']-btc['min_price']

if opening_price + fluctuation>btc['max_price']:
    print('상승장입니다')
else:
    print('하락장')


