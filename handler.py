from instagram import client, subscriptions
from conf import *
import json
from helper import respCleaner

class Calculate(object):
    FollowBack = []
    FollowMe = []
    Fans = []
    user_data = {}

    def __init__(self,access_token):
        api = client.InstagramAPI(access_token=access_token)

        user_follows, next = api.user_follows()
        self.FollowBack = [i for i in user_follows]

        while next:
            user_follows, next = api.user_follows(with_next_url=next)
            self.FollowBack += user_follows

        user_followed_by ,next = api.user_followed_by()
        self.FollowMe = [i for i in user_followed_by]

        while next:
            user_followed_by, next = api.user_followed_by(with_next_url=next)
            self.FollowMe += user_followed_by

    def calculate(self):
        for i in self.FollowBack:
            self.user_data[i.username] = dict(Username=i.username,Id=i.id,Fullname=i.full_name,Pic=i.profile_picture)

        for i in self.FollowMe:
            self.user_data[i.username] = dict(Username=i.username,Id=i.id,Fullname=i.full_name,Pic=i.profile_picture)

        self.FollowMe = [i.username for i in self.FollowMe]
        self.FollowBack = [i.username for i in self.FollowBack]

        self.NonFollowers = set(self.FollowBack).difference(self.FollowMe)

        self.Fans = set(self.FollowMe).difference(self.FollowBack)

    def get(self):
        self.calculate()


class MyFans(Calculate):
    def get(self):
        self.calculate()
        resp = [self.user_data.get(i) for i in self.Fans]
        return json.dumps(resp, indent=4)


class MyNonFollowers(Calculate):
    def get(self):
        self.calculate()
        self.NonFollowers = respCleaner(self.NonFollowers)
        resp = [self.user_data.get(i) for i in self.NonFollowers]
        return json.dumps(resp, indent=4)

class UserDetails(object):
    user = {}

    def __init__(self,access_token):
        api = client.InstagramAPI(access_token=access_token)
        info = api.user()
        self.user = dict(
            bio=info.bio,name=info.full_name,username=info.username,counts=info.counts,pic=info.profile_picture
        )

    def get(self):
        return json.dumps(self.user,indent=4)