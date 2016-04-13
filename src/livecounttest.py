import requests
from src.messenger import Messenger


def test_live_count():
    crow = Messenger()
    id_count_pairs = set()
    response = requests.get('http://api.varzesh3.com/v0.2/news/live/0').json()
    for item in response:
        id_count_pairs.add((item['Id'], item['ViewCount']))
    try:
        assert len(id_count_pairs) is len(response)
        crow.deliver("No Duplicates in http://api.varzesh3.com/v0.2/news/live/0")
    except Exception as ex:
        crow.deliver(str(ex))


if __name__ == '__main__':
    test_live_count()







