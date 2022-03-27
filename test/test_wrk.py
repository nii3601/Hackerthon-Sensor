import RPi.GPIO as GPIO
from gpiozero import LightSensor
from time import sleep
import time
import sys
import requests
import json
import http.client as httplib
import signal
import subprocess

url = 'https://parseapi.back4app.com/classes/water_use_scoreboard/'
appkey = 'XP2YymokHIQgloxN10YNdjgGY0s1q6Fzf4GhavKD'
restkey = 'NqMKcQLm8aLz79ibqtyOWWuxKqzTKeN6xplIMXCK'
headers = {'X-Parse-Application-Id': appkey, 'X-Parse-REST-API-Key': restkey}
objId = 'JHBJJfsioy'

volume = 0

def main():
    global volume
    GPIO.setmode(GPIO.BOARD)
    INPUT_PIN = 16
    GPIO.setup(INPUT_PIN, GPIO.IN)
    reading = 0
    lastReading = 0
    volume = 0

    signal.signal(signal.SIGUSR1, usr_handle)

    while (True):
        if (GPIO.input(INPUT_PIN) == 0):
            reading = 0
        else:
            reading = 1
        if (reading != lastReading):
            volume += 1.75
        lastReading = reading
        print(volume)

        sleep(0.01)

    return

def usr_handle(signum,frame):
    global volume
    global objId
    process = subprocess.Popen(['/home/hack/update.sh', f'{volume}'], text=True)
    volume = 0
    return
    result = requests.get(url, headers=headers)
    get = result.json()['results']
    update_water(get,objectId=objId,score=volume)

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
