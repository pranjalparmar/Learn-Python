import requests as r
from bs4 import BeautifulSoup as bs
import time
import webbrowser as w

URL = "https://www.flipkart.com/realme-x-polar-white-128-gb/p/itmfgybqzcgbxs26?pid=MOBFGYBQZUPWN4DF&lid=LSTMOBFGYBQZUPWN4DFN8MJJY&marketplace=FLIPKART&srno=b_1_9&otracker=nmenu_sub_Electronics_0_Realme&fm=neo%2Fmerchandising&iid=7d340780-1102-465d-ad21-0920120d36fe.MOBFGYBQZUPWN4DF.SEARCH&ppt=browse&ppn=browse&ssid=y6raymijkg0000001594432375207L"

while True:
    page = r.get(URL)
    soup = bs(page.content, "html.parser")

    # Use whatever you see in Inspect Element of the website this keeps changing from web page to webpage
    price = soup.find("div", {"class": "_1USjzt"}).text
    # Uncomment above line if you use Flipkart website

    # This is used to remove the ₹ symbol and get the price
    price = price[1:]

    # This is used to remove the , in between the prices to make it a number
    price_ar = price.split(",")
    price = ''.join(price_ar)

    # Conver the price which is string to an integer to compare
    price = int(price)

    print(price)

    # Use your comparing logic here below
    # Example:
    if price < 21000:
        w.open(URL)
        break

    # Any time you want it to wait to check next time. I gave 5 seconds
    time.sleep(5)