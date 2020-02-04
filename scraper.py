from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO



flag = input("Choose one of the following Scraper \n 1.Web Scraper \n 2.Image Scraper\n ")

search = input("Enter search keyword : ")
params = {"q": search}

if (flag=="1"):
    r = requests.get("http://www.bing.com/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find("ol", {"id" : "b_results"})
    links = results.findAll("li", {"class" : "b_algo"})

    for item in links:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]

        if item_text and item_href:
            print(item_text)
            print(item_href)
            print("Summary : ", item.find("a").parent.parent.find("p").text)
