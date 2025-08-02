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

    # to store potential liked pages and their score
    page_suggestions = {}


    for other_user, pages in user_pages.items():
    #other_user will be the user ID, and pages will be the set of pages they liked.
        if other_user != user_id:
            shared_pages = user_liked_pages.interaction(pages)
            for page in pages:
                if page not in user_liked_pages:
                    page_suggestions[page] = page_suggestions.get(page,0) + len(shared_pages)
                    
