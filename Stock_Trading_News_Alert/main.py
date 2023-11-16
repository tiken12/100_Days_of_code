import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


STOCK_API_KEY = "DV1F877V2Q1KP6CL" #Stock API
NEWS_API_KEY = "5597de40f3ba44b4b5cc25ebccff8659" #News API
TWILIO_SID = "AC10396d091497887cdc1e39ad7c5935f4" #Twilio SID
TWILIO_AUTH_TOKEN = "372d4c123739a8f9d5a7d5df80e5ca4e" #Auth Token
   
#Getting the stock prices from alphavantage
stock_params = {
   "function":"TIME_SERIES_DAILY",
   "symbol": STOCK_NAME,
   "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params= stock_params)
#print(response.json())
data = response.json()["Time Series (Daily)"]
#lets tap into the List Comprehension Keyword
#new_list = [new_item for item in list]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#The day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#Showing the difference from the two days closing price using absolute value
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
   up_down = 

# Print the difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent =(difference / float(yesterday_closing_price))*100
print(diff_percent)

# When percentage is greater than 5 the program will use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 1:
   news_params = {
      "apikey": NEWS_API_KEY,
      "qInTitle": COMPANY_NAME,
   }

   news_response = requests.get(NEWS_ENDPOINT, params=news_params)
   articles = news_response.json()["articles"]
   
#Using the slice operator to create a list that contains the first 3 articles.
   three_articles = articles[:3]
   #print(three_articles)
   
   
   #[new_item for item in list]
   formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
   print(formatted_articles)


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
   client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
   for article in formatted_articles:
      message = client.messages.create(
         body = article,
         from_ = "+18664902360",
         to = "+14078014121",
         
      )

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

