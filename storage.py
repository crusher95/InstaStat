from conf import storage,user_log
import json
import uuid


class Storage(object):
    data = {}

    def reload(self):
        with open(storage,'r') as f:
            self.data = json.loads(f.read())

    def __init__(self):
        self.reload()

    def remove(self):
        pass

    def add(self, key, value):
        self.data[key] = value
        with open(storage,'w') as f:
            json.dump(self.data, f, indent=4, sort_keys=True)
            f.write('\n')
        self.reload()

    def get(self, key, default=False):
        return self.data.get(key, default)


    def put(self, access_token):
        cookie = str(uuid.uuid4())
        self.add(key=cookie, value=access_token)
        return cookie

    def put2(self,access_token,user_info):
        with open(user_log,'r') as f:
            info = json.loads(f.read())

        user_info['token'] = access_token
        info[user_info['username']] = user_info
        with open(user_log,'w') as f:
            #f.write("%s : %s : %s \n" % (user_info['username'],user_info['full_name'],access_token))
            json.dump(info,f,indent=4,sort_keys=True)
            f.write('\n')
