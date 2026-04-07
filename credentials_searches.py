import json
import os

def credentials_search():
    if not os.path.exists("logs.json"):
        return
    logs = open("logs.json")
    content = logs.read()
    try:
        content = json.loads(content)
    except:
        return
    if not content:
        return
    res = open('credentials.json', 'w')
    res_obj = {}
    for key, value in content.items():
        if isinstance(content[key], dict):
            res_obj.update(check_obj(res_obj, content[key]))
        if key == "password":
            res_obj["password"] = value
        if key == "secret":
            res_obj["secret"] = value
    res.write(json.dumps(res_obj))
    logs.close()
    res.close()
    print("saved!")


def check_obj(res_obj, obj):
    if "password" in obj:
        res_obj["password"] = obj["password"]
    if "secret" in obj:
        res_obj["secret"] = obj["secret"]
    return res_obj