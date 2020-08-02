from urllib.request import urlopen, Request

url = "https://www.amazon.in/dp/B01MQU5LW7/"
requestingURL = Request(url, headers={'User-Agent' : "Magic Browser"}) 
page = urlopen(requestingURL).read()
page = str(page)

# print(page)

searchword = "<span class=\'a-color-price\'>"
possibleLocation = page.find(searchword)

# print(possibleLocation)

import re
regex = r'<span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">(.*?)</span>'
instances = re.findall(regex, page)
print(instances[0])


