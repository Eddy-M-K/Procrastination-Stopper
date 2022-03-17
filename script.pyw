import time
from datetime import datetime as dt

hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com", "www.messenger.com", "messenger.com", "www.snapchat.com", "snapchat.com", "www.twitch.tv", "twitch.tv", "www.reddit.com", "reddit.com", "www.ondemandkorea.com", "ondemandkorea.com", "twist.moe", "www.twitter.com", "twitter.com"]

while True:
    if (0 <= dt.today().weekday() <= 4):
        if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,12): 
            with open(hostsPath, 'r+') as file: 
                content = file.read() 
                for website in websites: 
                    if website in content: 
                        pass
                    else: 
                        # mapping hostnames to your localhost IP address 
                        file.write(redirect + " " + website + "\n") 
        elif dt(dt.now().year, dt.now().month, dt.now().day,13) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17,30): 
            with open(hostsPath, 'r+') as file: 
                content = file.read() 
                for website in websites: 
                    if website in content: 
                        pass
                    else: 
                        # mapping hostnames to your localhost IP address 
                        file.write(redirect + " " + website + "\n") 
        elif dt(dt.now().year, dt.now().month, dt.now().day,18,30) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22,30): 
            with open(hostsPath, 'r+') as file: 
                content = file.read() 
                for website in websites: 
                    if website in content: 
                        pass
                    else: 
                        # mapping hostnames to your localhost IP address 
                        file.write(redirect + " " + website + "\n") 
        else: 
            with open(hostsPath, 'r+') as file: 
                content=file.readlines() 
                file.seek(0) 
                for line in content: 
                    if not any(website in line for website in websites): 
                        file.write(line) 
    
                # removing hostnmes from host file 
                file.truncate() 
    else:
        if dt(dt.now().year, dt.now().month, dt.now().day,10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,12):  
            with open(hostsPath, 'r+') as file: 
                content = file.read() 
                for website in websites: 
                    if website in content: 
                        pass
                    else: 
                        # mapping hostnames to your localhost IP address 
                        file.write(redirect + " " + website + "\n") 
        elif dt(dt.now().year, dt.now().month, dt.now().day,13) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17,30):  
            with open(hostsPath, 'r+') as file: 
                content = file.read() 
                for website in websites: 
                    if website in content: 
                        pass
                    else: 
                        # mapping hostnames to your localhost IP address 
                        file.write(redirect + " " + website + "\n") 
        elif dt(dt.now().year, dt.now().month, dt.now().day,18,30) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22,30): 
            with open(hostsPath, 'r+') as file: 
                content = file.read() 
                for website in websites: 
                    if website in content: 
                        pass
                    else: 
                        # mapping hostnames to your localhost IP address 
                        file.write(redirect + " " + website + "\n") 
        else: 
            with open(hostsPath, 'r+') as file: 
                content=file.readlines() 
                file.seek(0) 
                for line in content: 
                    if not any(website in line for website in websites): 
                        file.write(line) 
    
                # removing hostnmes from host file 
                file.truncate() 
    time.sleep(5) 