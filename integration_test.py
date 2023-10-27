import unittest
from fastapi.testclient import TestClient
from main import app

class TestIntegrationAPI(unittest.TestCase):
    def test_get_total_online_time(self):
        client = TestClient(app)
        user_id = "df60f3f8-0e13-b64a-76b5-863bae54478e"
        response = client.get(f"/api/stats/user/total?user_id={user_id}")
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("totalTime", response_data)

    def test_get_average_online_time(self):
        client = TestClient(app)
        user_id = "df60f3f8-0e13-b64a-76b5-863bae54478e"
        response = client.get(f"/api/stats/user/average?user_id={user_id}")
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("weeklyAverage", response_data)
        self.assertIn("dailyAverage", response_data)

    def test_get_report(self):
        client = TestClient(app)
        report_name = "example_report"
        from_date = "2023-10-01"
        to_date = "2023-10-31"
        response = client.get(f"/api/report/{report_name}?from_date={from_date}&to_date={to_date}")
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

if __name__ == '__main__':
    unittest.main()
