import json;

def create_new_user(dict):
    new_dict = json.loads(dict)
    if 'username' not in new_dict or 'email' not in dict:
        return User()
    return User(new_dict['username'], new_dict['email'])

def user_to_json(user):
    return json.dumps(user.__dict__)
    
class User:
    def __init__(self, username = 'user', email = 'something@mail.com'):
        self.username = username
        self.email = email

registration_0 = '{"username": "mario", "email": "mario@me.it"}'
registration_1 = '{"city": "Rome", "country": "Italy"}'

user_0 = create_new_user(registration_0)
user_1 = create_new_user(registration_1)

print(user_to_json(user_0))
print(user_to_json(user_1))