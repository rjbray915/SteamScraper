import requests
API_KEY = "D331F1DEB5EDAE0D7CC90FA90B98852E"
#r = requests.get("http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=440&count=3&maxlength=300&format=json")
r = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v2/?key=" + API_KEY)

print(r.json())