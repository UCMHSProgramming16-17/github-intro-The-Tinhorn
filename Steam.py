import requests
import webbrowser
import json
import csv
style = input("What do you want to request: ")
base_url = 'http://api.steampowered.com/'
SteamID = input("What is your Steam ID: ")
key = '8E889E83A42C15D13E11EA54405CF63A'

if style.lower() == "achievements":
    appid = input("Enter AppID")
    url = base_url  + 'ISteamUserStats/GetPlayerAchievements/v0001/?appid=' + appid + '&key=' + key + '&steamid=' + SteamID
    
elif style.lower() == "recent games":
    url = base_url  + 'IPlayerService/GetRecentlyPlayedGames/v0001/?key=' + key + '&steamid=' + SteamID + '&format=json'
    
elif style.lower() == "player summary":
     url = base_url  + 'ISteamUser/GetPlayerSummaries/v0002/?key=' + key + '&steamids=' + SteamID 
     
elif style.lower() == "bans":
    url = base_url + 'ISteamUser/GetPlayerBans/v1/?key=' + key + '&steamids=' + SteamID
    
else:
    print("You can request: Bans, Achievements, Recent Games, and Player Summary")
    
    
    
    
#base_url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key='
def ID():
    print(url)

ID()
r=requests.get(url)
file = r.json()
#print(file)
infile = open("file", "r")
outfile = open("bar.csv", "w")
writer = csv.writer(outfile)
for row in json.loads(infile.read()):
    writer.write(row)
#My ID 76561198061868064
#BO3 AppID 311210