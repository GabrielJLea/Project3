# ebay-dl

##  What is `ebay-dl.py`?

`ebay-dl.py` is a script that scrapes ebay search result pages and extracts item listings into data formats such as JSON or CSV. 

For each item found on ebay, the script extracts:

- **name**: the name/title of the item  
- **price**: the price of the item in **cents**  
- **status**: whether the item is *Brand New*, *Pre-owned*, etc.  
- **shipping**: shipping cost in **cents** 
- **free_returns**: whether the item has free returns   
- **items_sold**: number of items sold 


---

## How to Run `ebay-dl.py`

## JSON format
To run, Enter the command below into the terminal and change (item) with the desired thing you are searching for, make sure the item is in quotation marks so that it recognizes spaces.

python ebay-dl.py ('item')

To change the number of pages (the base is 10) which are put into your JSON file, use the command below and change the variable PageNumbers with the desired number of pages.

python ebay-dl.py ('item') --num_pages=(PageNumbers)

Example of final command: python ebay-dl.py 'plane' --num_pages=4


## CSV format

csv uses the same form as the json command however you need to add (--csv) at the end of the command

Example of final csv command: python ebay-dl.py 'plane' --num_pages=4 --csv

## Link to Project
[Course Project GitHub Repository](https://github.com/mikeizbicki/cmc-csci040/tree/2025spring/project_03_webscraping)