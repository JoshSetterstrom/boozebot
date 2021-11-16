import requests, json
from bs4 import BeautifulSoup
from util.compare_json import compare_json

##Scrapes BSW Liquor site for new items and restocked items##
def scrape_bsw():
    print("Scraping bsw...")
    new_list = {"items": []}
    
    request = requests.get('https://www.bswliquor.com/whisky.html?limit=all')
    soup = BeautifulSoup(request.text, 'html.parser')
    items = soup.find("ul", {"class": "products-grid columns4 hide-addtolinks"}).findChildren("li")

    for item in items:
        ##Checks if item is in stock##
        if item.find("a", {"class": "addtocart outofstock"}): stock = False
        else: stock = True

        new_list['items'].append({
            "name": item.find("h2").text,
            "img": item.find("img")['src'],
            "link": item.find("h2").find("a")['href'],
            "stock": stock
        })

    with open("./data/bsw.json", "r+") as file: zyn = json.load(file)
    updates = compare_json(zyn, new_list)
    with open("./data/bsw.json", "w+") as file: json.dump(new_list, file, indent=2)

    return {"site": "BSW Liquor", "updates": updates}