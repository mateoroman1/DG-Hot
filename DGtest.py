import requests

post_request = {"requestId":"1a4015c8481a49b5beb6ac27d6f7a131","context":{"userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0","timeOffsetInMinutes":-300,"channel":"web","screen":{"width":1440,"height":900,"orientation":"landscape","colorDepth":30,"pixelRatio":2},"window":{"width":1440,"height":407},"browser":{"host":"www.dollargeneral.com","webGLRenderer":"Intel(R) HD Graphics 400"},"address":{"url":"https://www.dollargeneral.com/p/hot-wheels-basic-car-assorted/887961792461","referringUrl":"https://www.dollargeneral.com/product-search.html?q=hot+wheels"}},"id":{"tntId":"11c430b8912d45e799a62bc9ff7a4fd5.35_0","marketingCloudVisitorId":"91137920114397668539042242740741946368"},"experienceCloud":{"analytics":{"logging":"server_side","supplementalDataId":"525D2520F19E74C7-1DCB2F2F42B8B473"}},"execute":{"pageLoad":{"parameters":{"targetDynamicData_sLoggedIn":"logged out","targetDynamicData_customerID":"","targetDynamicData_pageUrl":"https://www.dollargeneral.com/p/hot-wheels-basic-car-assorted/887961792461","targetDynamicData_pageName":"Pickup Product Page","targetDynamicData_currentCategory":"","targetDynamicData_history":"","targetDynamicData_storeNumber":"4980","targetDynamicData_storeZip":"","entity.id":"","entity.cartIds":"","source":"targetDynamicData","webECID":"91137920114397668539042242740741946368","user.categoryId":"","currently_lapsed":"yes","entity.categoryId":"","entity.categoryName":"","customer_login_status":"logged out"}}},"prefetch":{"views":[{"parameters":{"targetDynamicData_sLoggedIn":"logged out","targetDynamicData_customerID":"","targetDynamicData_pageUrl":"https://www.dollargeneral.com/p/hot-wheels-basic-car-assorted/887961792461","targetDynamicData_pageName":"Pickup Product Page","targetDynamicData_currentCategory":"","targetDynamicData_history":"","targetDynamicData_storeNumber":"4980","targetDynamicData_storeZip":"","entity.id":"","entity.cartIds":"","source":"targetDynamicData","webECID":"91137920114397668539042242740741946368","user.categoryId":"","currently_lapsed":"yes","entity.categoryId":"","entity.categoryName":"","customer_login_status":"logged out"}}]}}
payload = {'_':'1679359634205', 'upc':'887961792461' , 'store':'4980' , 'magneto':'true', 'deviceId':'91137920114397668539042242740741946368', 'clientOriginStoreNumber':'' }


def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers, params=payload)
    print(page.status_code)
    print()
    return page.json()

def check_inventory():
    url = "https://www.dollargeneral.com/bin/omni/pickup/product/detail"
    page = get_page_html(url)
    productDetails = page.get('productDetails')
    print('Hot Wheels in stock:', productDetails.get('availableStock'))
    print('availableStockStore:', productDetails.get('availableStockStore'))
    print('Inventory status:', productDetails.get('inventoryStatus'))

payload['store'] = input('Enter store number:\n')
#4980 for Liberty\n12435 for Claycomo\n1207 for Excelsior Springs\n
check_inventory()