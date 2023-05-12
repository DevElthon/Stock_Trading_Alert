import requests
from twilio.rest import Client
from math import ceil

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "#KEY"
NEWS_API_KEY = "#KEY"
TWILIO_SID = "#KEY"
TWILIO_AUTH_TOKEN = "#TOKEN"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_prince = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_prince)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#diff_percent_to_compare usado apenas para placeholder pois os valores estão baixos
#o objetivo dessa modificação é não gerar um alerta enviesado
diff_percent_to_compare = ceil(abs((difference / float(yesterday_closing_price)) * 100))
diff_percent = abs((difference / float(yesterday_closing_price)) * 100)

#A porcentagem deve ser ajustada para o valor desejado.
#No momento a mesma esta com um valor "placeholder"
if diff_percent_to_compare > 0:
    news_params = {
        "apiKey":NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent:.2f}%\nHeadline : {article['title']}. \nBrief: {article ['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+TestNumber",
            to="+YOUR Number",
        )