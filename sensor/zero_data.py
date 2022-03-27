import sys
import requests
import json
import http.client as httplib

url = 'https://parseapi.back4app.com/classes/water_use_scoreboard/'
appkey = 'XP2YymokHIQgloxN10YNdjgGY0s1q6Fzf4GhavKD'
restkey = 'NqMKcQLm8aLz79ibqtyOWWuxKqzTKeN6xplIMXCK'
headers = {'X-Parse-Application-Id': appkey, 'X-Parse-REST-API-Key': restkey}

def main():
    result = requests.get(url, headers=headers)
    get = result.json()['results']
    zero_water(get)
    return

def zero_water(rows):
    Ids = []
    for obj in rows:
        Ids.append(obj['objectId'])

    for i in Ids:
        post_url = url+f'{i}/'
        post_headers = headers
        post_headers['Content-Type'] = 'application/json'
        post_obj = {'score': 0}

        result = requests.put(post_url, json=post_obj, headers=post_headers)
        print(result.status_code)
    return


if __name__ == '__main__':
    main()
