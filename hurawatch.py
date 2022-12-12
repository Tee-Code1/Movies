import requests
from bs4 import BeautifulSoup

# Send a GET request to the website and store the response
response = requests.get('https://hurawatch.at/movies?page=3')

url = 'https://hurawatch.at'

# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the specific elements you want to scrape
movie_elements = soup.find_all('div', class_='content')


my_list = []
info= []

# Loop through the movie elements and extract the data you want
for movie in movie_elements:
    title = movie.find_all('div', class_='item')
    for i in title:
        star = i.find("span", class_="imdb").text
        rating = float(star)
        if rating >= 8:
            titl = i.find('a',class_= 'title').text
            year = i.find('div', class_="meta").text
            pres= year[1:5]
            mint = year[6:14]
            
            
            image_tag = i.find('img')
            image_link = image_tag['src']
            urls = i.find('a', class_="poster")["href"]
            links = f'{url}{urls}'
            details = {"Title": titl,"Year" :pres , "Rating":rating, "Minutes": mint ,"Link":links, "ImageLink":image_link}
            info.append(details)


        
from twilio.rest import Client

# Set your Twilio account SID, auth token, and the WhatsApp number you want to send the message to
account_sid = 'ACd3ea68a2975e07507ee64e2f30e9148a'
auth_token = '854302900dcfeba421a83bea058f9148'
to_whatsapp_number = 'whatsapp:+2349075255792'

# Use the requests library to download the image
image_response = requests.get(image_link)

# Set the URL of the Twilio API endpoint and the image URL
api_url = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json'.format(account_sid)
media_url = image_link

# Set the headers and data for the API request



# Use the Twilio client to make the API request
client = Client(account_sid, auth_token)
for i in info:


    response = client.messages.create(
        to=to_whatsapp_number,
        from_='whatsapp:+14155238886',
        body=f'Today Recomended Movie to watch:{i["Title"]} \nmovie link is: {i["Link"]} \nMovie rating: {i["Rating"]} \nMovie duration: {i["Minutes"]}',
        media_url=i["ImageLink"],
    )