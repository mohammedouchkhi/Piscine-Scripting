import json;

def merge_two(first):
    dic = {}
    while 1:
        key = input("key: ")
        if key == "exit":
            break
        val = input("valeu: ")
        dic[key] = int(val)
    first.update(dic) 
    return json.dumps(first)