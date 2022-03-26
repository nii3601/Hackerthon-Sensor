import sys
import requests
import json
import http.client as httplib

url = 'https://parseapi.back4app.com/classes/water_use_scoreboard/'
appkey = 'XP2YymokHIQgloxN10YNdjgGY0s1q6Fzf4GhavKD'
restkey = 'NqMKcQLm8aLz79ibqtyOWWuxKqzTKeN6xplIMXCK'
headers = {'X-Parse-Application-Id': appkey, 'X-Parse-REST-API-Key': restkey}
objId = 'JHBJJfsioy'

def main():
    args = sys.argv
    #print(sys.argv)

    volume = float(sys.argv[1])
    result = requests.get(url, headers=headers)
    get = result.json()['results']
    update_water(get,objectId=objId,score=volume)

    return

def update_water(rows,objectId='',score=0):
    if objectId == '':
        return
    for obj in rows:
        if (obj['objectId'] == objectId):
            #score = obj['score']
            #print(f'score: {score}')
            #print(f'type(score): {type(score)}')
            score += obj['score']
            obj['score'] = score
            #print(f'score: {score}')
            #print(obj)
            post_url = url+f'{objectId}/'
            post_headers = headers
            post_headers['Content-Type'] = 'application/json'
            #print(post_url)
            #print(post_headers)
            #post_obj = {'className': 'water_use_scoreboard', 'score': score, 'objectId': objectId}
            post_obj = {'score': score}
            result = requests.put(post_url, json=post_obj, headers=post_headers)
            print(result.status_code)
            return

if __name__ == '__main__':
    main()

