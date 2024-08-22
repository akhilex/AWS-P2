import requests
import unittest

class TestAPIIntegration(unittest.TestCase):

    API_ENDPOINT = "https://your-api-id.execute-api.region.amazonaws.com/prod"  # Replace with your actual endpoint

    def test_api_integration(self):
        response = requests.get(self.API_ENDPOINT)
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json()['body'], ["yes", "no", "maybe"])

if __name__ == '__main__':
    unittest.main()
