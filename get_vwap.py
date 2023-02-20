import json
import requests
from bs4 import BeautifulSoup


url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=SKIPPER&illiquid=0&smeFlag=0&itpFlag=0'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}

soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
data = json.loads(soup.select_one('#responseDiv').text)

# uncomment this to print all data:
# print(json.dumps(data, indent=4))

print('averagePrice:', data['data'][0]['averagePrice'])
