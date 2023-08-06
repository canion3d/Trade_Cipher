import requests
import streamlit

url = "https://seeking-alpha-finance.p.rapidapi.com/v1/search/advanced"

querystring = {"query":"bill","search_advanced_type":"people"}

headers = {
	"X-RapidAPI-Key": "d29531ae60msh09b292159b1d570p1db262jsnd2039bec5d98",
	"X-RapidAPI-Host": "seeking-alpha-finance.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

headers = {
	"X-RapidAPI-Key": "d29531ae60msh09b292159b1d570p1db262jsnd2039bec5d98",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

import http.client

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "62b008b623mshaf55ca1e208d945p1256acjsn8ca0e82661f6",
    'X-RapidAPI-Host': "alpha-vantage.p.rapidapi.com"
}

conn.request("GET", "/query?interval=5min&function=TIME_SERIES_INTRADAY&symbol=MSFT&datatype=json&output_size=compact", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
