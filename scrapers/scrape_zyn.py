import requests, json
from bs4 import BeautifulSoup
from util.compare_json import compare_json

##Scrapes ZYN site for new items and restocked items##
def scrape_zyn():
    print("Scraping zyn...")
    new_list = {"items": []}
    
    ##Navigates each page on site for all items##
    for i in range(1, 1000):
        request = requests.get(f'https://zyn.ca/collections/whisky?sort=created-descending&page={i}')
        soup = BeautifulSoup(request.text, 'html.parser')
        items = soup.find_all("div", {"class": "inner-top"})

        ##This site removes items if it not in stock, so no need to check for "out of stock" elements##
        if not items: break

        for item in items:
            new_list['items'].append({
                "name": item.find("div", {"class": "product-bottom"}).find('a').text.replace('\n', '').lstrip(' ').rstrip(' '),
                "img": f'https://{item.find("div", {"class": "product-top"}).find("img")["data-src"][2:]}',
                "link": f"https://zyn.ca{item.find('div', {'class': 'product-bottom'}).find('a')['href']}",
                "stock": True
            })

    with open("./data/zyn.json", "r+") as file: zyn = json.load(file)
    updates = compare_json(zyn, new_list)
    with open("./data/zyn.json", "w+") as file: json.dump(new_list, file, indent=2)

    return {"site": "ZYN", "updates": updates}