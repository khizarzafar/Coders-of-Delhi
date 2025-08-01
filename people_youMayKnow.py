import json

def data_load(filename):
    with open(filename,'r') as f:
        return json.load(f)



def find_people_you_may_know(user_id,data):
    pass


data = data_load("data.json")
user_id = 1
recc = find_people_you_may_know(user_id,data)
print(recc)
