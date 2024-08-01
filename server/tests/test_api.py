import unittest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import patch, MagicMock
from routes.tasks import router

app = FastAPI()
app.include_router(router)

class TestTasksAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Response": "Up and running"})

    @patch('routes.tasks.redis_client')
    @patch('routes.tasks.crawler_task')
    def test_submit_crawling_task_cached(self, mock_crawler_task, mock_redis):
        mock_redis.get.return_value = b"http://cached-url.com"
        
        response = self.client.post("/crawl", json={"url": "http://example.com", "max_ttr": "dummy"})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"task_id": "", "sitemap_url": "http://cached-url.com"})
        mock_crawler_task.delay.assert_not_called()

    @patch('routes.tasks.redis_client')
    @patch('routes.tasks.crawler_task')
    def test_submit_crawling_task_new(self, mock_crawler_task, mock_redis):
        mock_redis.get.return_value = None
        mock_task = MagicMock()
        mock_task.id = "test_task_id"
        mock_crawler_task.delay.return_value = mock_task
        
        response = self.client.post("/crawl", json={"url": "http://example.com", "max_ttr": "dummy"})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"task_id": "test_task_id", "sitemap_url": ""})
        mock_crawler_task.delay.assert_called_once()

    @patch('routes.tasks.crawler_task')
    def test_get_status_pending(self, mock_crawler_task):
        mock_task = MagicMock()
        mock_task.state = "PENDING"
        mock_crawler_task.AsyncResult.return_value = mock_task
        
        response = self.client.get("/tasks/test_task_id")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "task_id": "test_task_id",
            "status": "PENDING",
            "timestamp": None,
            "input_url": None,
            "sitemap_url": None,
            "error_message": None
        })

    @patch('routes.tasks.crawler_task')
    def test_get_status_success(self, mock_crawler_task):
        mock_task = MagicMock()
        mock_task.state = "SUCCESS"
        mock_task.result = {"sitemap_url": "http://example.com/sitemap.xml", "input_url": "http://example.com"}
        mock_crawler_task.AsyncResult.return_value = mock_task
        
        response = self.client.get("/tasks/test_task_id")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "task_id": "test_task_id",
            "status": "SUCCESS",
            "timestamp": "",
            "input_url": "http://example.com",
            "sitemap_url": "http://example.com/sitemap.xml",
            "error_message": None
        })

    @patch('routes.tasks.crawler_task')
    def test_get_status_failure(self, mock_crawler_task):
        mock_task = MagicMock()
        mock_task.state = "FAILURE"
        mock_task.input_url = "http://example.com"
        mock_task.error_message = "Test error message"
        mock_crawler_task.AsyncResult.return_value = mock_task
        
        response = self.client.get("/tasks/test_task_id")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "task_id": "test_task_id",
            "status": "FAILURE",
            "timestamp": "",
            "input_url": "http://example.com",
            "sitemap_url": "",
            "error_message": "Test error message"
        })

if __name__ == '__main__':
    unittest.main()
