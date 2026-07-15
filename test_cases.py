import unittest
from app import app

class HelloTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_status_code(self):
        response = self.client.get('/api/hello')
        self.assertEqual(response.status_code, 200)

    def test_hello_json_content(self):
        response = self.client.get('/api/hello')
        data = response.get_json()
        self.assertEqual(data, {"message": "hello world 2", "status": "ok"})

if __name__ == '__main__':
    unittest.main()