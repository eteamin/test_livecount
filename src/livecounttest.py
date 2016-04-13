import requests
import unittest
from src.messenger import Messenger


class Test(unittest.TestCase):
    def test_live_count(self):
        crow = Messenger()
        id_count_pairs = set()
        response = requests.get('http://api.varzesh3.com/v0.2/news/live/0').json()
        for item in response:
            id_count_pairs.add((item['Id'], item['ViewCount']))
        try:
            self.assertEqual(len(id_count_pairs), len(response))
            crow.deliver("No Duplicates in http://api.varzesh3.com/v0.2/news/live/0")
        except Exception as ex:
            crow.deliver(str(ex))


if __name__ == '__main__':
    unittest.main()











