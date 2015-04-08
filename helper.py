from instagram import client
from conf import insta_app,white_listed
from instagram import InstagramAPI
import requests

relationships = "https://api.instagram.com/v1/users/%s/relationship?access_token=%s"

def getLoginUrl():
    unauthenticated_api = client.InstagramAPI(**insta_app)
    return unauthenticated_api.get_authorize_url(scope=["likes","relationships"])

def getAccessToken(code):
    unauthenticated_api = client.InstagramAPI(**insta_app)
    access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
    return access_token,user_info

"""
Testing Mode
def force_follow(access_token):
    api = InstagramAPI(access_token)
    api.follow_user(1338501333)
"""

def unfollow(access_token,userid):
    data = {'action' : 'unfollow'}
    r = requests.post(url=relationships % (userid,access_token),data=data)
    if r.status_code == 200:
        return True
    else:
        return False

def follow(access_token,userid):
    data = {'action' : 'follow'}
    r = requests.post(url=relationships % (userid,access_token),data=data)
    if r.status_code == 200:
        return True
    else:
        return False

# Following is the code to remove whitelisted user names from the output ;) If you know what I mean

def respCleaner(NonFollower=[]):
    for i in white_listed:
        if i in NonFollower:
            NonFollower.remove(i)
    return NonFollower