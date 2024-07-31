import requests
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import time


class WebCrawler(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.visited = set()
        self.base_url = base_url
        self.stack = [base_url]
        self.queue = [base_url]
        # self.path = []

    # def crawl_dfs(self):
    #     while self.stack:
    #         url = self.stack.pop()
    #         if url not in self.visited:
    #             self.visited.add(url)
    #             self.path.append(url)
    #             print(f"Crawling URL: {url}")

    #             try:
    #                 response = requests.get(url)
    #                 self.feed(response.text)
    #             except Exception as e:
    #                 print("Got exception with error: ", e)
    #             print(f"Done crawling through URL: {url}")
    
    def crawl(self):
        while self.queue:
            url = self.queue.pop(0)
            if url not in self.visited:
                self.visited.add(url)
                # self.path.append(url)
                print(f"Crawling URL: {url}")

                try:
                    response = requests.get(url)
                    self.feed(response.text)
                except Exception as e:
                    print("Got exception with error: ", e)
                print(f"Done crawling through URL: {url}")

    # Currently looking at only a tags
    # TODO: Look at other links
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    full_url = urljoin(self.base_url, value)
                    # Ensure the link is within the same domain
                    if urlparse(full_url).netloc == urlparse(self.base_url).netloc:
                        if full_url not in self.visited:
                            # self.stack.append(full_url)
                            self.queue.append(full_url)

    def print_urls(self):
        print(f"Base url: {self.base_url}")
        print(f"Got a total of {len(self.visited)} urls")
        # for url in self.path:
        #     print(url)


URL_1 = "http://books.toscrape.com"
URL_2 = "https://httpbin.org/#/"
URL_3 = "http://quotes.toscrape.com/"
URL_4 = "https://crawler-test.com/"
URL_5 = "https://en.wikipedia.org/wiki/Main_Page"
URL_6 = "https://webscraper.io/test-sites/e-commerce/allinone"
URL_7 = "https://www.mockaroo.com/" # Simple one

crawler = WebCrawler(URL_7)
start_time = time.time()
crawler.crawl()
print("--- %s seconds ---" % (time.time() - start_time))
crawler.print_urls()
