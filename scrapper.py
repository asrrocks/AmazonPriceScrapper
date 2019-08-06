import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Test-Exclusive-606/dp/B07HGJK535/ref=sr_1_1?crid=236P6LFYX778I&keywords=oneplus+7+pro&qid=1565089143&s=gateway&smid=A23AODI1X2CEAE&sprefix=one+pl%2Caps%2C288&sr=8-1'

headers = {
    "User-Agent": '[Google - My useragent and copy it here]'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

title = soup.find(id="productTitle").get_text()
print(title.strip())
price = soup.find(id="priceblock_dealprice").get_text()
converted_price = float(price[2:4])


def check_price():
    if(converted_price < 53):
        send_mail()
    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('[Your EmailID]', '[password]')

    subject = 'Price fell Down'
    body = 'Check the price https://www.amazon.in/Test-Exclusive-606/dp/B07HGJK535/ref=sr_1_1?crid=236P6LFYX778I&keywords=oneplus+7+pro&qid=1565089143&s=gateway&smid=A23AODI1X2CEAE&sprefix=one+pl%2Caps%2C288&sr=8-1'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        '[Your EmailID]',
        '[Your Other EmailID]',
        msg
    )
    print('Hey email has been sent')
    server.quit()


check_price()
