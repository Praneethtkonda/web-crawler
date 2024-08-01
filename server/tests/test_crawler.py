import unittest
from util.crawler import WebCrawler

class TestWebCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = WebCrawler("http://example.com")
        self.crawler.crawl()

    def test_crawl(self):
        # Assuming the WebCrawler has a method to set a mock HTML content
        self.assertEqual(len(self.crawler.visited), 1)
        # Asserting to 1 because the other link is external link

    def test_export_site_map(self):
        # Assuming the WebCrawler has a method to set a mock HTML content
        sitemap = self.crawler.export_site_map()
        self.assertIsInstance(sitemap, dict)

if __name__ == '__main__':
    unittest.main()
