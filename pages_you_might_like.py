import json

def load_data(filename):
    with open(filename,'r') as f:
        return json.load(f)
    
def pages_you_might_like(user_id,data):
    #dict to store user interacted pages
    user_pages = {}
    for user in data['users']:
        user_pages[user['id']] = set(user['liked_pages'])
        # After all iterations, user_pages becomes:
        # {
        #     1: {101},
        #     2: {102},
        #     3: {101, 103},
        #     4: {104}
        # }

    if user_id not in user_pages:
        return []
    
    user_liked_pages = user_pages[user_id]
    # user_liked_pages is now {101}.

    