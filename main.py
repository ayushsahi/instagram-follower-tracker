import instaloader

L = instaloader.Instaloader()

USER = ''
PASSWORD = ''
following_list = []
follower_list = []


def login(user: str, password: str) -> None:
    USER = user
    PASSWORD = password
    L.login(USER, PASSWORD) 

def get_followers() -> None:
    profile = instaloader.Profile.from_username(L.context, USER)

    for followee in profile.get_followers():
        follower_list.append(followee.username)
    
    # print(follower_list)
    print(len(follower_list))

def get_following() -> None:
    profile = instaloader.Profile.from_username(L.context, USER)

    for follower in profile.get_following():
        following_list.append(follower.username)

    # print(following_list)
    print(len(following_list))


if __name__ == "__main__":
    login('ayushsahi', 'M0nk3y10!_Instagram')
    get_followers()
    get_following()
