# DG-Hot
a simple script that checks Dollar General's website to view the number of currently in stock Hot Wheels mainline cars

Need latest version of python installed, as well as requests

for requests:
pip install requests

or

https://requests.readthedocs.io/en/latest/

How to use:
1. Run the DGtest.py file
2. Enter store number (for how to find store number see below) e.g. 12344
3. Program will return the current stock information for that specific store


How to find store #

1. Go to https://www.dollargeneral.com/store-locator
2. click View Details under the store you want to check
3. In the URL, after the city name will be a number, this is that locations store number
    e.g. https://www.dollargeneral.com/store-directory/ar/little-rock/12344 is store 12344
