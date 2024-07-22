import json
from colorama import *
import json
import random
from decrypt import decrypt_key, send_request

with open('config.json', 'r') as f:
    configs = json.load(f)

# Change Colors Of tools Style
def main_color():
    with open('config.json', 'r') as f:
        config = json.load(f)
    style = config['style']
    if style == 1:
        color = Fore.BLUE
    elif style == 2:
        color = Fore.GREEN
    elif style == 3:
        color = Fore.RED
    elif style == 4:
        color = Fore.YELLOW
    elif style == 5:
        color = Fore.MAGENTA
    elif style == 6:
        color = Fore.CYAN
    elif style == 7:
        color = Fore.WHITE
    else:
        return
    return color

# Snusbase API
def api_email(email):
    search_response = send_request('data/search', {
        'terms': [email],
        'types': ["email"],
        'wildcard': False,
    })
    return search_response

def api_username(username):
    search_response = send_request('data/search', {
        'terms': [username],
        'types': ["username"],
        'wildcard': False,
    })
    return search_response

def api_password(password):
    search_response = send_request('data/search', {
        'terms': [password],
        'types': ["password"],
        'wildcard': False,
    })
    return search_response

def api_name(name):
    search_response = send_request('data/search', {
        'terms': [name],
        'types': ["name"],
        'wildcard': False,
    })
    return search_response


def api_hash(hash_value):
    search_response = send_request('data/search', {
        'terms': [hash_value],
        'types': ["hash"],
        'wildcard': False,
    })
    return search_response

def api_ip(ip):
    search_response = send_request('data/search', {
        'terms': [ip],
        'types': ["lastip"],
        'wildcard': False,
    })
    return search_response

# token spammer 
def nonce_generator(length=19):
    return ''.join(str(random.randint(1, 9)) for _ in range(length))


# username lookup links
def api_links(username):
    api_list = [
        f"https://api.instantusername.com/c/instagram/{username}",
        f"https://api.instantusername.com/c/tiktok/{username}",
        f"https://api.instantusername.com/c/x-(twitter)/{username}",
        f"https://api.instantusername.com/c/facebook/{username}",
        f"https://api.instantusername.com/c/snapchat/{username}",
        f"https://api.instantusername.com/c/reddit/{username}",
        f"https://api.instantusername.com/c/youtube/{username}",
        f"https://api.instantusername.com/c/twitch/{username}",
        f"https://api.instantusername.com/c/vimeo/{username}",
        f"https://api.instantusername.com/c/rumble/{username}",
        f"https://api.instantusername.com/c/dailymotion/{username}",
        f"https://api.instantusername.com/c/linkedin/{username}",
        f"https://api.instantusername.com/c/slack/{username}",
        f"https://api.instantusername.com/c/fiverr/{username}",
        f"https://api.instantusername.com/c/github/{username}",
        f"https://api.instantusername.com/c/gitlab/{username}",
        f"https://api.instantusername.com/c/steamgroup/{username}",
        f"https://api.instantusername.com/c/xbox-gamertag/{username}",
        f"https://api.instantusername.com/c/minecraft/{username}",
        f"https://api.instantusername.com/c/lichess/{username}",
        f"https://api.instantusername.com/c/chess.com/{username}",
        f"https://api.instantusername.com/c/dribbble/{username}",
        f"https://api.instantusername.com/c/behance/{username}",
        f"https://api.instantusername.com/c/redbubble/{username}",
        f"https://api.instantusername.com/c/artstation/{username}",
        f"https://api.instantusername.com/c/lottiefiles/{username}",
        f"https://api.instantusername.com/c/medium/{username}",
        f"https://api.instantusername.com/c/wordpress/{username}",
        f"https://api.instantusername.com/c/blogger/{username}",
        f"https://api.instantusername.com/c/deviantart/{username}",
        f"https://api.instantusername.com/c/slides/{username}",
        f"https://api.instantusername.com/c/roblox/{username}",
        f"https://api.instantusername.com/c/osu!/{username}",
        f"https://api.instantusername.com/c/google-playstore/{username}",
        f"https://api.instantusername.com/c/tetr.io/{username}",
        f"https://api.instantusername.com/c/hackernews/{username}",
        f"https://api.instantusername.com/c/trello/{username}",
        f"https://api.instantusername.com/c/docker-hub/{username}",
        f"https://api.instantusername.com/c/replit.com/{username}",
        f"https://api.instantusername.com/c/codecademy/{username}",
        f"https://api.instantusername.com/c/leetcode/{username}",
        f"https://api.instantusername.com/c/hackerrank/{username}",
        f"https://api.instantusername.com/c/codepen/{username}",
        f"https://api.instantusername.com/c/dev-community/{username}",
        f"https://api.instantusername.com/c/opensource/{username}",
        f"https://api.instantusername.com/c/hackerone/{username}",
        f"https://api.instantusername.com/c/hashnode/{username}",
        f"https://api.instantusername.com/c/gitbook/{username}",
        f"https://api.instantusername.com/c/fosstodon/{username}",
        f"https://api.instantusername.com/c/chaos/{username}",
        f"https://api.instantusername.com/c/geeksforgeeks/{username}",
        f"https://api.instantusername.com/c/kaggle/{username}"
    ]
    return api_list