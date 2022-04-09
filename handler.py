import os
import urllib.request
import json

def hello(event, context):

    url = 'https://api.line.me/v2/bot/message/broadcast'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.environ['ACCESS_TOKEN']
    }

    data = {
        'messages': [
            {
                'type': 'text',
                'text': '宿題やってますか？',
            }
        ]
    }

    req = urllib.request.Request(url=url, data=json.dumps(data).encode('utf-8'), method='POST', headers=headers)
        
    with urllib.request.urlopen(req) as res:

        print(res.read().decode("utf-8"))