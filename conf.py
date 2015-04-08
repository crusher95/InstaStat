import json

with open('conf.json') as f:
    conf = json.loads(f.read())

webconfig = conf.get("webconfig")

insta_app = conf.get("insta_app")

storage = conf.get("storage")

user_log = conf.get("user_log")

json_header = conf.get("json_header")

html_header = conf.get("html_header")

white_listed = conf.get("white_listed")

DBconnection = conf.get("DBconnection")