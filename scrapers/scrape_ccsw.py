import requests, json
from bs4 import BeautifulSoup
from util.compare_json import compare_json

##Scrapes Craft Cellars site for new items and restocked items##
def scrape_ccsw():
    print("Scraping ccsw...")
    request = requests.get('https://craftcellars.ca/product-category/whisky/scotch-whisky/page/1/?orderby=date')
    soup = BeautifulSoup(request.text, 'html.parser')
    page_total = int(soup.find("ul", {"class": "page-numbers"}).findChildren(recursive=False)[-2].text)
    new_list = {"items": []}

    #Navigates each page on site for all items##
    for i in range(1, page_total+1):
        request = requests.get(f'https://craftcellars.ca/product-category/whisky/scotch-whisky/page/{i}/?orderby=date')
        soup = BeautifulSoup(request.text, 'html.parser')

        items = soup.find("div", {"data-source": "main_loop"}).findChildren("div", recursive=False)

        for item in items:
            ##Checks if item is in stock##
            if item.find("span", {"class": "out-of-stock product-label"}): stock = False
            else: stock = True

            new_list['items'].append({
                "name": item.find("h3").text,
                "img": item.find("div", {"class": "product-list-image product-element-top"}).find("img")['src'],
                "link": item.find("div", {"class": "product-list-image product-element-top"}).find("a")['href'],
                "stock": stock,
            })

    with open("./data/ccsw.json", "r+") as file: ccsw = json.load(file)
    updates = compare_json(ccsw, new_list)
    with open("./data/ccsw.json", "w+") as file: json.dump(new_list, file, indent=2)
    
    return {"site": "Craft Cellars", "updates": updates}