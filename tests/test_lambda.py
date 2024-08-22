import unittest
from src.lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def test_lambda_handler(self):
        event = {}
        context = {}
        response = lambda_handler(event, context)
        
        # Check status code
        self.assertEqual(response['statusCode'], 200)
        
        # Check if the response body is either 'yes', 'no', or 'maybe'
        self.assertIn(response['body'], ["yes", "no", "maybe"])

if __name__ == '__main__':
    unittest.main()
