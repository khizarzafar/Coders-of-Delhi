import json

def load_data(filename):
    with open(filename,'r') as f:
        return json.load(f)
    
def pages_you_might_like(user_id,data):
    #dict to store user interacted pages
