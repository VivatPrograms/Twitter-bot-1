import tweepy,time
from keys import *

cooldown = 2*60 # This is the cooldown time frame in seconds between posts 2*60 = 120 seconds, change it if you want
last_run = -cooldown
index = 0
m = []
minus = False

message = ['placeholder','GUYS CONTROVERSIAL OPINION WHY DO WE EXIST?','https://www.youtube.com/watch?v=WSrlFDzWcSc']
#For every message there should be a text and image, 
#if no text then leave it None for example message = [None,'text',..], the same is true for image variable, leave it None if no image
#you can add as many messages and images as u want, not only 3. But both arrays should have the same amount of elements (right now its 3 elements)
image = ['.venv\cat.jpg',None,None]

def api():
    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_token_secret)
    return tweepy.API(auth)

def tweet(api:tweepy.API,message:str,image_path=None):
    if minus: api.destroy_status(m[index])
    if image_path:
        return api.update_status_with_media(message,image_path)
    else:
        return api.update_status(message)

if __name__ == '__main__':
    api = api()
    for i in range(len(message)): m.append(None)
    while True:
        if time.time()-last_run >= cooldown:
            t = tweet(api,message[index],image[index])
            m[index] = t.id 
            if index == len(message)-1: minus,index = True,0
            elif index < len(message)-1: index += 1
            last_run = time.time()
