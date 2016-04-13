import requests


class Messenger(object):
    def __init__(self):
        self.token = 'xoxp-13319976114-20556087794-31577611078-8f47cd840d'
        self.receiving_channel = '@amin'

    def deliver(self, text):
        message = {
            'token': self.token,
            'text': text,
            'channel': self.receiving_channel
        }
        response = requests.post('http://crow.farakav.com/api/message', json=message)
        print(response.json())