import unittest
from seventh_homework.feature.main import calculate_total_online_time, calculate_average_online_time


class TestYourFunctions(unittest.TestCase):

    def test_calculate_total_online_time(self):
        user_id = "df60f3f8-0e13-b64a-76b5-863bae54478e"
        user_data = [
            {"userId": "df60f3f8-0e13-b64a-76b5-863bae54478e", "lastSeenDate": "2023-10-20T10:00:00Z"},
            {"userId": "0d0ac023-746e-5d8e-3229-4b049c62400c", "lastSeenDate": "2023-10-20T08:00:00Z"},
        ]
        result = calculate_total_online_time(user_id, user_data)
        self.assertEqual(result, 7200)

    def test_calculate_average_online_time(self):
        user_id = "cd9a0c70-c32e-defb-55b0-8014d079ad54"
        user_data = [
            {"userId": "a69de642-dd03-ba60-2241-9952b57463ef", "lastSeenDate": "2023-10-20T10:00:00Z"},
            {"userId": "ee3cfee1-5c6e-d2e7-77ff-d2695844dac4", "lastSeenDate": "2023-10-19T12:00:00Z"},
            {"userId": "cd9a0c70-c32e-defb-55b0-8014d079ad54", "lastSeenDate": "2023-10-20T08:00:00Z"},
        ]
        weekly_average, daily_average = calculate_average_online_time(user_id, user_data)
        self.assertEqual(weekly_average, 54000)
        self.assertEqual(daily_average, 18000)

if __name__ == '__main__':
    unittest.main()
