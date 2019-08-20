import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4R8QGM/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+a7&qid=1566296312&s=gateway&sr=8-5'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])
    if(converted_price < 1.800):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server =  smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('andrei.cimpoes@student.usv.ro', 'zgrctjcgldgzgsnh')
    