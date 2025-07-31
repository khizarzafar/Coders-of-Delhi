import json

def cleanData(data):
    #remove missing spaces
    data['user'] = [user for user in data['users'] if user ['name'].strip()]
    # remove duplicate friends
    for user in data['users']:
        user['friends'] = list(set(user['friends']))
    return data



data = json.load(open("data2.json"))
data = cleanData(data)
json.dump(data, open("cleaned_data2.json","w"),indent=4)
print("Data has been successfully cleaned.")