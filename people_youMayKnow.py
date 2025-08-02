import json

def data_load(filename):
    with open(filename,'r') as f:
        return json.load(f)



def find_people_you_may_know(user_id,data):

    #!Step 1: We find all friends of a user and and store them in user_friends dictionary...
    user_friends = {}
    for user in data['users']:
        user_friends[user['id']] = set(user['friends']) 
    #   After this loop, the user_friends dictionary looks like this:
    #   {1: {2, 3}, 2: {1, 4}, 3: {1}, 4: {2}, 5: set()}    

    if user_id not in user_friends:
        return []
    
    #!Step 2: Identifying direct friends...
    direct_friends = user_friends[user_id]
    #   This line retrieves the set of friends for user_id 1
    #   direct_friends is now {2,3}

    suggestions = {}
    #   An empty dict to store mutual friend counts

    #!Step 3: Finding Friends of Friends
    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in direct_friends:
                suggestions[mutual] = suggestions.get(mutual,0) + 1
                #   The suggestions dictionary becomes {4: 1}





data = data_load("data.json")
user_id = 1
recc = find_people_you_may_know(user_id,data)
print(recc)
