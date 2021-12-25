import instaloader

L = instaloader.Instaloader()

USER = 'ayushsahi'
PASSWORD = ''
following_list = []
follower_list = []

def login() -> None:
    L.login(USER, PASSWORD) 

def get_followers() -> None:
    profile = instaloader.Profile.from_username(L.context, USER)

    for followee in profile.get_followers():
        follower_list.append(followee.username)
    
    # print(follower_list)
    print(len(follower_list))

def get_following() -> None:
    profile = instaloader.Profile.from_username(L.context, USER)

    for follower in profile.get_followees():
        if follower.is_verified is False:
            following_list.append(follower.username)

    # print(following_list)
    print(len(following_list))

def generate_users_not_following_back() -> list:
    output = []
    for user in following_list:
        if user not in follower_list:
            output.append(user)

    print(output)
    return output

if __name__ == "__main__":
    login()
    get_followers()
    get_following()
    generate_users_not_following_back()

