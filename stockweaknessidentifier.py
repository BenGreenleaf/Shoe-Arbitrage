import requests, json

cookies = {
    'stockx_device_id': '86c93efe-1c2f-4f55-a500-256fa9af6146',
    'stockx_session_id': 'c412e26d-8e3c-42ce-ac69-b95d607ac28f',
    'stockx_session': '73002238-a17a-45b5-9f69-8e10a6292fef',
    'language_code': 'en_gb',
    'stockx_selected_region': 'GB',
    '_pxhd': '3APDF8MAS4vWXgGnE7FbWCyWe1RM8cW0vXX9jZb9l39DH6fz-9xD/0c47r2qxOG-37uJelkh7dW-RfvBKp5Lyg==:a1g4AQ9jPwT/MkkWxVmEJDdOmSFX3uL185CU-KHYLgjXdnXoMsd8xGJUfBMZ/olCXnl9pzkawnSJ8EeWNSbwqY9iKzRljaJhwy3Q6e9T2iI=',
    'display_location_selector': 'false',
    'chakra-ui-color-mode': 'light',
    'cf_clearance': 'tUXnb0jnK6A373tVsuKAHzNBRYzvqxiUIBpiNeLok7A-1708194807-1.0-ASTcVUkF9gBaJ0BFI793ohTfsC63JKm6VtyT5M16Ih4nT5MXR1tM+WMdYwZ1MqBfSz69pbGhF7VcqScJXbYWcVw=',
    '__ssid': '436d8643d00bb720d9a1fa731e5708a',
    'ftr_blst_1h': '1708194815968',
    'QuantumMetricSessionID': '78ec587a26a94b455d313d8bad054c54',
    'QuantumMetricUserID': 'c4249222196583b45f1c9a77dbf1dd19',
    'stockx_preferred_market_activity': 'sales',
    'stockx_homepage': 'sneakers',
    'stockx_product_visits': '2',
    'OptanonAlertBoxClosed': '2024-02-17T18:47:45.139Z',
    'ajs_user_id': 'cced36f3-29e8-11eb-a20e-124738b50e12',
    'ajs_anonymous_id': '634a96ba-18f4-4bed-bf3b-5500912d20c6',
    'rbuid': 'rbos-7adfa8ce-d450-4df8-b9ce-fba82c6ed5b4',
    '__cf_bm': 'Rmg8VSOgYIjYKh9LNUaZFClFSGSSiZQZC_gK6fXe5Jw-1708195707-1.0-Aez4I9N0m2aNt/1IfyZoIkyweEXxJKAO7TnBMGdWztVfLBrmKyqqofPRnXa2Md0ehoqI6tha3H1TLc4E5RNgTvA=',
    'is_gdpr': 'true',
    'stockx_ip_region': 'GB',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Feb+17+2024+18%3A48%3A57+GMT%2B0000+(Greenwich+Mean+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1ef08d64-bd3e-40a7-bbdc-484a8da5616b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0005%3A1%2CC0004%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=GB%3BENG',
    'forterToken': '10fb11fbab454627ac888703dd695a3b_1708195738084__UDF43-m4_13ck',
    '_dd_s': 'rum=0&expire=1708196753588&logs=1&id=4ffdf9cd-9e25-4b04-846a-1d4657198a86&created=1708194813898',
}



def stockxCheck(slug):

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'stockx_device_id=86c93efe-1c2f-4f55-a500-256fa9af6146; stockx_session_id=c412e26d-8e3c-42ce-ac69-b95d607ac28f; stockx_session=73002238-a17a-45b5-9f69-8e10a6292fef; language_code=en_gb; stockx_selected_region=GB; _pxhd=3APDF8MAS4vWXgGnE7FbWCyWe1RM8cW0vXX9jZb9l39DH6fz-9xD/0c47r2qxOG-37uJelkh7dW-RfvBKp5Lyg==:a1g4AQ9jPwT/MkkWxVmEJDdOmSFX3uL185CU-KHYLgjXdnXoMsd8xGJUfBMZ/olCXnl9pzkawnSJ8EeWNSbwqY9iKzRljaJhwy3Q6e9T2iI=; display_location_selector=false; chakra-ui-color-mode=light; cf_clearance=tUXnb0jnK6A373tVsuKAHzNBRYzvqxiUIBpiNeLok7A-1708194807-1.0-ASTcVUkF9gBaJ0BFI793ohTfsC63JKm6VtyT5M16Ih4nT5MXR1tM+WMdYwZ1MqBfSz69pbGhF7VcqScJXbYWcVw=; __ssid=436d8643d00bb720d9a1fa731e5708a; ftr_blst_1h=1708194815968; QuantumMetricSessionID=78ec587a26a94b455d313d8bad054c54; QuantumMetricUserID=c4249222196583b45f1c9a77dbf1dd19; stockx_preferred_market_activity=sales; stockx_homepage=sneakers; stockx_product_visits=2; OptanonAlertBoxClosed=2024-02-17T18:47:45.139Z; ajs_user_id=cced36f3-29e8-11eb-a20e-124738b50e12; ajs_anonymous_id=634a96ba-18f4-4bed-bf3b-5500912d20c6; rbuid=rbos-7adfa8ce-d450-4df8-b9ce-fba82c6ed5b4; __cf_bm=Rmg8VSOgYIjYKh9LNUaZFClFSGSSiZQZC_gK6fXe5Jw-1708195707-1.0-Aez4I9N0m2aNt/1IfyZoIkyweEXxJKAO7TnBMGdWztVfLBrmKyqqofPRnXa2Md0ehoqI6tha3H1TLc4E5RNgTvA=; is_gdpr=true; stockx_ip_region=GB; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+17+2024+18%3A48%3A57+GMT%2B0000+(Greenwich+Mean+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1ef08d64-bd3e-40a7-bbdc-484a8da5616b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0005%3A1%2CC0004%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=GB%3BENG; forterToken=10fb11fbab454627ac888703dd695a3b_1708195738084__UDF43-m4_13ck; _dd_s=rum=0&expire=1708196753588&logs=1&id=4ffdf9cd-9e25-4b04-846a-1d4657198a86&created=1708194813898',
    'Referer': 'https://stockx.com/en-gb',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-nextjs-data': '1',
    }

    json_data = {
        'query': 'query GetProductPriceLevels($productId: String!, $market: String, $currencyCode: CurrencyCode, $transactionType: TransactionType, $page: Int, $limit: Int, $enableAIAPrices: Boolean, $isVariant: Boolean!) {\n  product(id: $productId) @skip(if: $isVariant) {\n    id\n    market(currencyCode: $currencyCode) {\n      ...MarketPriceLevelsFragment\n    }\n  }\n  variant(id: $productId) @include(if: $isVariant) {\n    id\n    market(currencyCode: $currencyCode) {\n      ...MarketPriceLevelsFragment\n    }\n  }\n}\n\nfragment MarketPriceLevelsFragment on Market {\n  priceLevels(\n    market: $market\n    transactionType: $transactionType\n    page: $page\n    limit: $limit\n    enableAIAPrices: $enableAIAPrices\n  ) {\n    edges {\n      node {\n        count\n        ownCount\n        amount\n        variant {\n          id\n          traits {\n            size\n          }\n        }\n      }\n    }\n  }\n}',
        'variables': {
            'productId': slug,
            'market': 'GB',
            'currencyCode': 'GBP',
            'transactionType': 'BID',
            'page': 1,
            'limit': 50,
            'enableAIAPrices': True,
            'isVariant': False,
        },
        'operationName': 'GetProductPriceLevels',
    }

    response = requests.post('https://stockx.com/api/p/e', cookies=cookies, headers=headers, json=json_data)

    highest = 0

    data = {}
    print(json.loads(response.content))
    for i in json.loads(response.content)['data']['product']['market']['priceLevels']['edges']:
        t = i['node']

        try:
            if t['amount'] > data[t['variant']['traits']['size']]:
                data[t['variant']['traits']['size']] = t['amount']
        except:
            data[t['variant']['traits']['size']] = t['amount']

    return(data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"query":"query GetProductPriceLevels($productId: String!, $market: String, $currencyCode: CurrencyCode, $transactionType: TransactionType, $page: Int, $limit: Int, $enableAIAPrices: Boolean, $isVariant: Boolean!) {\\n  product(id: $productId) @skip(if: $isVariant) {\\n    id\\n    market(currencyCode: $currencyCode) {\\n      ...MarketPriceLevelsFragment\\n    }\\n  }\\n  variant(id: $productId) @include(if: $isVariant) {\\n    id\\n    market(currencyCode: $currencyCode) {\\n      ...MarketPriceLevelsFragment\\n    }\\n  }\\n}\\n\\nfragment MarketPriceLevelsFragment on Market {\\n  priceLevels(\\n    market: $market\\n    transactionType: $transactionType\\n    page: $page\\n    limit: $limit\\n    enableAIAPrices: $enableAIAPrices\\n  ) {\\n    edges {\\n      node {\\n        count\\n        ownCount\\n        amount\\n        variant {\\n          id\\n          traits {\\n            size\\n          }\\n        }\\n      }\\n    }\\n  }\\n}","variables":{"productId":"nike-dunk-low-retro-white-black-2021","market":"GB","currencyCode":"GBP","transactionType":"BID","page":1,"limit":50,"enableAIAPrices":true,"isVariant":false},"operationName":"GetProductPriceLevels"}'
#response = requests.post('https://stockx.com/api/p/e', cookies=cookies, headers=headers, data=data)