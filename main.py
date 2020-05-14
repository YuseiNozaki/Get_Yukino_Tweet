import json
from requests_oauthlib import OAuth1Session
from config import ck, cs, at, ats


with open('since_id.txt', 'r') as f:
    since_id = int(f.read())

twitter = OAuth1Session(ck, cs, at, ats)

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

params = {
    'screen_name': 'ykn_1214',
    'count': 200,
    'since_id': since_id
}

req = twitter.get(url, params = params)

if req.status_code == 200:
    tweet_list = json.loads(req.text)

    if tweet_list == []:
        print('The latest tweets have already been retrieved.')

    else:        
        for tweet in tweet_list:
            week, month, day, time, _, year = tweet['created_at'].split()

            print(tweet['text'])
            print(f'{year}/{month}/{day}/{time}')
            print()

        latest_id_str = tweet_list[0]['id_str']

        with open('since_id.txt', 'w') as f:
            f.write(latest_id_str)

else:
    print(f'Faled: {req.status_code}')
