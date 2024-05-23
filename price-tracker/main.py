import smtplib
import os
import requests
from bs4 import BeautifulSoup
import dotenv

product_url = ("https://www.amazon.ca/HyperX-Cloud-III-Ultra-Clear-USB/dp/B0C3BSZ56D/ref=pd_ci_mcx_pspc_dp_d_2_t_1"
               "?pd_rd_w=RLb2Z&content-id=amzn1.sym.cc9b306e-f54a-42a9-af24-d836ac9ed640&pf_rd_p=cc9b306e-f54a-42a9"
               "-af24-d836ac9ed640&pf_rd_r=Z1AFHKY1YBT4BPT26DFG&pd_rd_wg=QcbzT&pd_rd_r=7ca64f22-88dc-4db4-843e"
               "-25699ce6e09e&pd_rd_i=B0C3BSZ56D&th=1")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en-IN;q=0.9,en;q=0.8",
}

# Getting product webpage from amazon
res = requests.get(url=product_url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')

# Extracting the price of the product
price_whole = soup.find('span', class_='a-price-whole').getText()
price_decimal = soup.find('span', class_='a-price-fraction').getText()
price = float(price_whole + price_decimal)

BUY_PRICE = 200

# Sending price alerts through gmail
if price < BUY_PRICE:
    dotenv.load_dotenv()
    smtp_addr = 'smtp.gmail.com'
    username = "meoz.test@gmail.com"
    from_addr = 'meoz.test@gmail.com'
    to_addr = 'itsrabio7@gmail.com'
    title = soup.find(id="productTitle").get_text().strip()
    sub = 'Amazon Price Alert!'
    msg = f"{title} is now {price}"

    with smtplib.SMTP(smtp_addr, port=587) as connection:
        connection.starttls()
        res = connection.login(username, os.getenv('PASSWORD'))
        connection.sendmail(
            from_addr,
            to_addr,
            msg=f"Subject: {sub}\n\n{msg}\n{product_url}".encode('utf-8')
        )
