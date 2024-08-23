from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_fortune_teller(self):
        self.client.get("/prod")

termimal of locust:
locust -f locustfile.py --host=https://your-api-id.execute-api.region.amazonaws.com
