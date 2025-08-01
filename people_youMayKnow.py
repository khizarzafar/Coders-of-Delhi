import json

def data_load(filename):
    with open(filename,'r') as f:
        return json.load(f)



def find_people_you_may_know(user_id,data):
    #Step 1: We find all friends of user_id 1 and and store them in user_friends dictionary...
    user_friends = {}
    for user in data['users']:
        user_friends[user['id']] = set(user['friends']) 
#   After this loop, the user_friends dictionary looks like this:
#   {1: {2, 3}, 2: {1, 4}, 3: {1}, 4: {2}, 5: set()}


data = data_load("data.json")
user_id = 1
recc = find_people_you_may_know(user_id,data)
print(recc)
