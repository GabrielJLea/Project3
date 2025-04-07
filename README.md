# ebay-dl

## 📦 What is `ebay-dl.py`?

`ebay-dl.py` is a script that scrapes eBAy search result pages and extracts item listings into data formats such as JSON or CSV. 

For each item found on eBay, the script extracts:

- **name**: the name/title of the item  
- **price**: the price of the item in **cents**  
- **status**: whether the item is *Brand New*, *Pre-owned*, etc.  
- **shipping**: shipping cost in **cents** 
- **free_returns**: whether the item has free returns   
- **items_sold**: number of items sold 


---

##  How to Run `ebay-dl.py`

# JSON format
To run, Enter the commanc below into the terminal and change (item) with the desired thing you are searching for.

python ebay-dl.py (item)

# CSV format