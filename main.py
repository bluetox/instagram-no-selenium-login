import requests

SUCCESFUL = "\033[32mSUCCESFUL\033[0m:"
ERROR = "\033[31mERROR\033[0m:"

#Just simple headers did you know that you can set your Cookie and CSRF token to NULL and still use the api
headers = {
    "Accept": "*/*",
    "Accept-Language": "fr-FR,fr;q=0.9",
    "Cache-Control": "no-cache",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "NULL",
    "Pragma": "no-cache",
    "Referer": "https://www.instagram.com/",
    "Sec-Ch-Prefers-Color-Scheme": "dark",
    "Sec-Ch-Ua": '"Opera GX";v="111", "Chromium";v="125", "Not.A/Brand";v="24"',
    "Sec-Ch-Ua-Full-Version-List": '"Opera GX";v="111.0.5168.54", "Chromium";v="125.0.6422.143", "Not.A/Brand";v="24.0.0.0"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "X-Csrftoken" : "NULL"
}

#Gathers Cookie and CSRF token anyways
def SetupSession():
    try:
        url = "https://www.instagram.com"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"{ERROR} Couldn't connect to instagram")
            
    except:
        print(f"{ERROR} No wifi")
    headers = response.headers
    try : 
        Cookie = headers['Set-Cookie']
        CookieParts = Cookie.split(';')
        for part in CookieParts:
            if "csrftoken" in part:
                csrftoken = part.split('=')[1].strip()
        headers["X-Csrftoken"] = csrftoken
        headers["Cookie"] = Cookie
        print(f"{SUCCESFUL} Cookies set up")
    except:
        print(f"{ERROR} Couldn't find the cookies")

#logs into instagram using the encrypted password
def Login():
    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    data = {
        "enc_password": f"{enc_password}",
        "optIntoOneTap": "false",
        "queryParams": "{}",
        "trustedDeviceRecords": "{}",
        "username": f"{username}"
    }
    response = requests.post(url,headers=headers,data=data)
    if response.json()['authenticated'] == True:
        print(f"{SUCCESFUL} Logged in")
    else:
        print(f"{ERROR} Couldn't log-in")

    try:
        Cookies = response.headers["Set-Cookie"].split()
        for part in Cookies:
            name = part.split('=')[0].strip()
            if name == "sessionid":
                headers["Cookie"] = f"sessionid={part.split('=')[1].strip()}"
        print(f"{SUCCESFUL} Connected to the session")
    except:
        print(f"{ERROR} Couldn't log into the session")
    
enc_password = input("Paste your encrypted password here: ")
username = input("Enter your username: ")
SetupSession()
Login()