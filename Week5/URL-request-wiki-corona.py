from urllib.request import urlopen, Request

url = "https://www.worldometers.info/coronavirus/country/india/"
requestingURL = Request(url, headers={'User-Agent' : "Magic Browser"}) 
page = urlopen(requestingURL).read()
page = str(page)

# print(page)

searchword = '<span style="color:#aaa">'
possibleLocation = page.find(searchword)

# print(possibleLocation)

import re
regex = r'<span style="color:#aaa">(.*?)</span>'
instances = re.findall(regex, page)
print(instances[0])


