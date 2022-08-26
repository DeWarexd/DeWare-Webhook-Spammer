from discord_webhook import DiscordWebhook
import random
from time import sleep
import pyfade
import os
from sys import platform

webhooktxt = open("WebHook.txt", "r")
WebHook_url = webhooktxt.read()
spaces = len(WebHook_url) * "─"

while True:
    os.system('cls')
    print(pyfade.Fade.Vertical(pyfade.Colors.purple_to_blue, f'''
    ▓█████▄ ▓█████  ██░ ██  ▒█████   ▒█████   ██ ▄█▀
    ▒██▀ ██▌▓█   ▀ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
    ░██   █▌▒███   ▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
    ░▓█▄   ▌▒▓█  ▄ ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
    ░▒████▓ ░▒████▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
    ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
    ░ ▒  ▒  ░ ░  ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
    ░ ░  ░    ░    ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
    ░       ░  ░ ░  ░  ░    ░ ░      ░ ░  ░  ░     by Denolaks
    ░    
    ┌─────────────│DeHook Features│─────────────┐
    │WebHook Spammer                            │
    ├───────────────────────────────────────────┤
    │https://github.com/Denolaks                │
    ├───────────────────────────────────────────┤
    │Working 2022                               │
    ├───────────────────────────────────────────┤
    │discord.gg/HXCxmc4G4J                      │
    └───────────────────────────────────────────┘
    ┌──────────{spaces}┐
    │WebHook: {WebHook_url} │
    └──────────{spaces}┘
    '''))

    Contents = [
        "Spam text",
        "Deno Siker"
    ]

    HowMuch = int(input(pyfade.Fade.Vertical(pyfade.Colors.purple_to_blue, "How much times do you want to spam: ")))
    Interval = float(input(pyfade.Fade.Vertical(pyfade.Colors.purple_to_blue, "Spam Interval: ")))
    Username = input(pyfade.Fade.Vertical(pyfade.Colors.purple_to_blue, "WebHook Username: "))
    ProfilePicture = input(pyfade.Fade.Vertical(pyfade.Colors.purple_to_blue, "WebHook Picture URL (Right click to paste or leave empty.): "))

    if Username == "" or " ":
        Username = "DeHook Discord Spammer"

    print(pyfade.Fade.Vertical(pyfade.Colors.purple_to_blue,f'''
    \n    ╔═══════════════════DeHook═══════════════════╗\n
    How much times will program spam: {HowMuch}
    Spam Interval: {Interval}
    Usernamel: {Username}
    Content: {' '.join(Contents)}\n
    ╚═══════════════════DeHook═══════════════════╝\n\n'''))


    for i in range(HowMuch):
        for items in Contents:
            if ProfilePicture == "" or " ":
                webhook = DiscordWebhook(url=WebHook_url, content=items, username=Username)
            webhook = DiscordWebhook(url=WebHook_url, content=items, username=Username, avatar_url=ProfilePicture)
            print(pyfade.Fade.Vertical(pyfade.Colors.purple_to_blue,f"Message sent: {WebHook_url}, {items}."))
            sleep(Interval)
            response = webhook.execute()