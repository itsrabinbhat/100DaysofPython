import requests
from bs4 import BeautifulSoup

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


