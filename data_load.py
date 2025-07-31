import json


# Function to load data from json file
def load_data(filename):
    with open(filename,"r") as f:
        data = json.load(f)
    return data

data = load_data("data.json")

# Function to display the users and their liked pages
def display_users(data):
    print("\nUsers connections:")
    for user in data['users']:
        print(f"ID:{user['id']} - {user['name']} is friends with {user['friends']} and their liked pages are {user['liked_pages']}.")
    print("\nPages information:")
    for page in data['pages']:
        print(f"{page['id']}: {page['name']}")

display_users(data)
