import sys
import signal
import time
import requests
import json

val = 0

def usr_handle(one,two):
    global val 
    val = 0

def main():
    global val

    signal.signal(signal.SIGUSR1, usr_handle)

    while (1):
        print(val)
        val += 1
        time.sleep(.1)

    return

if __name__ == '__main__':
    main()
