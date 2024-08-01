# Server


# Running the server

# Problems faced

Since this is automated code the scripts gets rate limited 

Looking only at <a></a> tags

Inconsistent crawling because of concurrency and locking mechanism

Pending items:-
Fix inconsistency in crawling
Not listing external links( Ideal behaviour is to not crawl them but list them)

sitemap builder code is listing more links

Build sitemap
Write Flask API
Create Redis
Integrate with celery
Have a nosql db
Add basic auth (stretch goal)

Statistics
For URL_1 (http://books.toscrape.com):-
Normal create.py
--- 538.582955121994 seconds ---
Base url: http://books.toscrape.com
Got a total of 746 urls

With multithreading
Run-2
--- 131.35121178627014 seconds ---
Base url: http://books.toscrape.com
Got a total of 721 urls

Run-1
--- 131.580659866333 seconds ---
Base url: http://books.toscrape.com
Got a total of 716 urls


For URL_3 (quotes.toscrape):-
Normal create.py:-


With multithreading
--- 46.738271951675415 seconds ---
Base url: http://quotes.toscrape.com/
Got a total of 214 urls

--- 165.7075228691101 seconds ---
Base url: http://quotes.toscrape.com/
Got a total of 214 urls




--- 30.967243909835815 seconds ---
Base url: https://webscraper.io/test-sites/e-commerce/allinone
Got a total of 575 urls
Site map exported to site_map.json

--- 78.78387308120728 seconds ---
Base url: https://webscraper.io/test-sites/e-commerce/static/product/126
Got a total of 559 urls
Site map exported to site_map.json


--- 12.655555009841919 seconds ---
Base url: https://www.mockaroo.com/
Got a total of 57 urls
Site map exported to site_map.json
