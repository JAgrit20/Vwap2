import requests
import json
from bs4 import BeautifulSoup
stockcode = "TATAELXSI"
print(stockcode)
stock_url  = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stockcode)
print(stock_url)
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(stock_url, headers=headers)
# response
soup = BeautifulSoup(response.text, 'html.parser')
data_array = soup.find(id='responseDiv').getText()

y = json.loads(data_array)

print(y['data'][-1]['lastPrice'])
