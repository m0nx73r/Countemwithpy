import urllib.request
import json
import sys
import time

name = input("Enter channel name : ")
ask_api = input('Do you have api? \n Type Y if you have API key : ')

if ask_api == 'y' or 'Y':
    pass
else:
    print('How to get your API : \n https://developers.google.com/youtube/v3/getting-started')
    sys.exit()

            
api = input('enter your api key : ')
t = input('Interval of Output \n [DEFAULT 1] :')
if t == '':
    t = int('1')
else:
    t = int(t)
    
while True:
    data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&key=' + (api) + '&forUsername=' + (name)).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    num = (name + " has " + "{:,d}".format(int(subs)) + " subscribers!")
    sys.stdout.write(num + '\n')
    time.sleep(t)
