import json

def get_recipes(file_name):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return json.loads(content)