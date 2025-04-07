import argparse
import requests
from bs4 import BeautifulSoup
import json
import csv
#get command line arguments
parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON')
parser.add_argument('search_term')
parser.add_argument('--num_pages', default = 10)
parser.add_argument('--csv', action='store_true')
args = parser.parse_args()
print(args.search_term)

# build URL
items = []
for page_number in range(1,int(args.num_pages)+1):
    url = 'https://www.ebay.com/sch/i.html?_nkw='
    url +=  args.search_term 
    url += '&_sacat=0&_from=R40&_pgn='
    url += str(page_number)
    print('url=', url)

    #download the Html
    r = requests.get(url)
    status = r.status_code
    print('status=', status)
    html = r.text

    #process the html
    soup = BeautifulSoup(html, 'html.parser')
    #loop over items in page 
    tags_items = soup.select('.s-item')
    for tag_item in tags_items:

        #extract name
        tags_name = tag_item.select('.s-item__title')
        name = None
        for tag in tags_name:
            name = tag.text

        #extract items sold
        items_sold = None
        tags_sold = tag_item.select('.s-item__quantitySold')
        for tag in tags_sold:
            items_sold = ''
            for digit in tag.text:
                if digit.isdigit():
                    items_sold += digit
        
        #extract price of item
        price = 0
        tags_price= tag_item.select('.s-item__price')
        for tag in tags_price:
            price_cents = ''
            for digit in tag.text:
                if digit.isdigit():
                    price_cents += digit
        if price_cents:
            price = int(price_cents)
        
        #extract shipping price
        shipping = 0
        tags_shipping = tag_item.select('.s-item__logisticsCost')
        for tag in tags_shipping:
            shipping = ''
            for digit in tag.text:
                if digit.isdigit():
                    shipping += digit
            if len(shipping) == 0:
                shipping = 0
        
        #extract status 
        status = False
        tags_status = tag_item.select('.SECONDARY_INFO')
        for tag in tags_status:
            status = tag.text

        #extract free returns
        free_returns = False
        tags_freereturns = tag_item.select('.s-item__free-returns')
        for tag in tags_freereturns:
            free_returns = True
        item = {
            'name': name,
            'price': price,
            'status': status,
            'shipping': int(shipping),
            'free_returns': free_returns,
            'items_sold': items_sold
        }
        items.append(item)

            

    print(len(tags_items))
    print(len(items))


#write the json or csv file 
if args.csv:
    filename = args.search_term + '.csv'
    if items:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=items[0].keys())
            writer.writeheader()
            writer.writerows(items)
else:
    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))