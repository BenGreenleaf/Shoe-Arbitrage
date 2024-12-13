import requests, json
from bs4 import BeautifulSoup
import sys
sys.path.insert(1, 'D:/Downloads')
import stockweaknessidentifier

response = requests.get("https://www.solespy.co.uk/_next/data/B4dEb9D_sLvG9S1KRvSTc/index.json")

for card in json.loads(response.content)['pageProps']['data']:
    data = {}
    ext = card['slug']
    print(ext )
    response = requests.get(
        'https://www.solespy.co.uk/_next/data/B4dEb9D_sLvG9S1KRvSTc/sneaker/'+str(ext)+'.json',
    )
    platformData = json.loads(response.content)['pageProps']['shoeData']['price']

    stockxSlug = json.loads(response.content)['pageProps']['shoeData']['platformData']['stockx']['slug']

    for platform in platformData:
        pName = platform['platform']

        for size in platform['prices']:
            try:
                data[size].append([pName, float(platform['prices'][size])])
            except:
                data[size] = []
                data[size].append([pName, float(platform['prices'][size])])


    stockxData = stockweaknessidentifier.stockxCheck(stockxSlug)

    n = 0
    for size in data.values():
        sizeOfShoe = list(data.keys())[n]
        lowest = [0, 10000000000]
        for listing in size:
            price = listing[1]
            platform = listing[0]
            if price != 0:
                if price < lowest[1]:
                    lowest = listing

        if lowest[0] != "stockx" and lowest[1] != 0:
            try:
                sellp = float(stockxData[sizeOfShoe])
                if sellp - lowest[1] > (sellp*0.09):
                    print(ext, sizeOfShoe, lowest[0], lowest[1], sellp, (sellp-lowest[1])-(sellp*0.09))

            except:
                pass



        n+= 1
