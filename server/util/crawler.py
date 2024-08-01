import requests
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
# import time
import threading
from queue import Queue
import concurrent.futures
import json
import random
from util.constants import USER_AGENTS

class WebCrawler(HTMLParser):
    def __init__(self, base_url, max_threads=5):
        super().__init__()
        self.base_url = base_url
        self.visited = set()
        self.queue = Queue()
        self.queue.put(base_url)
        self.max_threads = max_threads
        self.lock = threading.Lock()
        self.site_map = {base_url: []}
        self.current_url = None

    def crawl(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            while not self.queue.empty():
                futures = []
                for _ in range(min(self.queue.qsize(), self.max_threads)):
                    url = self.queue.get()
                    if url not in self.visited:
                        future = executor.submit(self.process_url, url)
                        futures.append(future)
                    else:
                        self.queue.task_done()
                concurrent.futures.wait(futures)

    def process_url(self, url):
        with self.lock:
            if url in self.visited:
                return
            self.visited.add(url)
            print(f"Crawling URL: {url}")

        try:
            headers = {'User-Agent': random.choice(USER_AGENTS)}
            response = requests.get(url, headers=headers)
            self.current_url = url
            self.site_map[url] = []
            self.feed(response.text)

            with self.lock:
                for link in self.site_map[url]:
                    if link not in self.visited:
                        self.queue.put(link)
        except Exception as e:
            print(f"Got exception with error: {e}")

        print(f"Done crawling through URL: {url}")
        self.queue.task_done()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    full_url = urljoin(self.current_url, value)
                    if urlparse(full_url).netloc == urlparse(self.base_url).netloc:
                        with self.lock:
                            self.site_map[self.current_url].append(full_url)

    def print_urls(self):
        print(f"Base url: {self.base_url}")
        print(f"Got a total of {len(self.visited)} urls")

    def print_site_map(self):
        print("Site Map:")
        print(self.site_map)

    def export_site_map(self):
        return self.site_map

    def export_site_map_json(self, filename="site_map.json"):
        with open(filename, 'w') as f:
            json.dump(self.site_map, f, indent=2)
        print(f"Site map exported to {filename}")

# Dry run
# URL_1 = "http://books.toscrape.com"
# URL_2 = "https://httpbin.org/#/"
# URL_3 = "http://quotes.toscrape.com/"
# URL_4 = "https://crawler-test.com/"
# URL_5 = "https://en.wikipedia.org/wiki/Main_Page"
# URL_6 = "https://webscraper.io/test-sites/e-commerce/allinone"
# URL_7 = "https://www.mockaroo.com/" # Simple one

# crawler = WebCrawler(URL_7, max_threads=10)
# start_time = time.time()
# crawler.crawl()
# print("--- %s seconds ---" % (time.time() - start_time))
# crawler.print_urls()
# # crawler.print_site_map()
# crawler.export_site_map_json()