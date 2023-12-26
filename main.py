import requests
import json
from colorama import init, Fore, Style

init(autoreset=True)

with open("usernames.txt", "r") as file:
    usernames = file.read().splitlines()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "authority": "discord.com",
}

url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"

available_usernames = []

for username in usernames:
    data = {
        "username": username
    }

    print(f"{Fore.LIGHTBLUE_EX}Checking username: {Fore.YELLOW}{username}{Style.RESET_ALL}")

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        if not response_json.get("taken", False):
            available_usernames.append(username)
            print(f"Status: {Fore.GREEN}Available!{Style.RESET_ALL}")
        else:
            print(f"Status: {Fore.RED}Taken{Style.RESET_ALL}")
    else:
        response_json = json.loads(response.text)
        if "message" in response_json and response_json["message"] == "The resource is being rate limited.":
            print(f"Status: {Fore.RED}You are being rate limited!{Style.RESET_ALL}")
        else:
            print(f"Status: {Fore.RED}Error{Style.RESET_ALL}")


with open("available_usernames.txt", "w") as output_file:
    for username in available_usernames:
        output_file.write(username + "\n")

print(f"{Fore.GREEN}Available usernames saved to available_usernames.txt{Style.RESET_ALL}")
