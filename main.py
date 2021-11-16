import time
from scrapers.scrape_bsw import scrape_bsw
from scrapers.scrape_ccaw import scrape_ccaw
from scrapers.scrape_ccsw import scrape_ccsw
from scrapers.scrape_zyn import scrape_zyn
from util.create_element import create_element
from util.send_email import send_email

def main():
    while True:
        for method in [scrape_bsw(), scrape_ccaw(), scrape_ccsw(), scrape_zyn()]:
            elements = ""

            for update in method['updates']['new']:
                elements = elements + create_element("Now in stock", update)

            for update in method['updates']['updated']:
                try:
                    if update['stock']: elements = elements + create_element("Now in stock", update)
                except: pass

            if bool(elements): send_email(method['site'], elements)
        
        time.sleep(300)

main()