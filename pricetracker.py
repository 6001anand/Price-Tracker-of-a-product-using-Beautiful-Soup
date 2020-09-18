import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/Mi-XMSH05HM-Band-3-Black/dp/B07HCXQZ4P?pf_rd_p=406d1302-20ad-5b8d-a279-43ce0bfbba6f&pf_rd_r=44VMT9Q8XN0KGNZBF1PF&pd_rd_wg=fedXC&ref_=pd_gw_ri&pd_rd_w=muoO3&pd_rd_r=20e78e14-dd07-44b1-b69a-678c73dc73b0'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


def checkprice():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soup1 = BeautifulSoup(soup.prettify(), "html.parser")

    title = soup1.find(id="productTitle").get_text()
    price = soup1.find(id="priceblock_dealprice").get_text().strip().replace(',', '')
    con_price = float(price[2:7])
    if(con_price > 1500):
        send_mail()
    print(con_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('64.233.184.108', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("6001anand.atre@gmail.com", "xlxypzlycvexyvva")
    subject = "the price fell down"
    body = "check link https://www.amazon.in/Mi-XMSH05HM-Band-3-Black/dp/B07HCXQZ4P?pf_rd_p=406d1302-20ad-5b8d-a279-43ce0bfbba6f&pf_rd_r=44VMT9Q8XN0KGNZBF1PF&pd_rd_wg=fedXC&ref_=pd_gw_ri&pd_rd_w=muoO3&pd_rd_r=20e78e14-dd07-44b1-b69a-678c73dc73b0"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        '6001anand.atre@gmail.com',
        'coolanand.atre@gmail.com',
        msg
    )
    print("mail sent")

    server.quit()


checkprice()