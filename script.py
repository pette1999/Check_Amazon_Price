import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/Samsung-970-EVO-Plus-MZ-V7S1T0B/dp/B07MFZY2F2/ref=sr_1_3?dchild=1&keywords=samsung+970+evo&qid=1594860637&sr=8-3"

headers = {"User-Agent": 'DISPLAY= /opt/google/chrome-remote-desktop/start-host --code="4/1wE8x_OSWGLdMhXK5mR0Ktf_wt3hegfZilnGntKyb5sUAXqdbP_NW6UXx24BpL01IiqhkhVfORp6Js9TjdYx-SQ" --redirect-url="https: // remotedesktop.google.com/_/oauthredirect" --name=$(hostname)'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:].strip())
    
    print(converted_price)

    if(converted_price < 190):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('meiguo1969@gmail.com', 'rbhxjpdcmvmqwfaj')

    subject = "Price Fell Down!"
    body = "Check the Amazon link => https://www.amazon.com/Samsung-970-EVO-Plus-MZ-V7S1T0B/dp/B07MFZY2F2/ref=sr_1_3?dchild=1&keywords=samsung+970+evo&qid=1594860637&sr=8-3"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'meiguo1969@gmail.com',
        'chenhaifan19991113@gmail.com',
        msg
    )

    print("Emial has been sent.")
    server.quit()
    
while(True):
    check_price()
    time.sleep(60)
    
