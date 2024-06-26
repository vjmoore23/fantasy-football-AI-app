import requests
import pandas as pd
import json


url = "https://api.sportradar.com/nfl/official/trial/v7/en/teams/ebd87119-b331-4469-9ea6-d51fe3ce2f1c/full_roster.json?api_key=ndMTecIz2D2DRf1c2xWL46QRx6brsxPM2C0JxhZR"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
print("======================================================================================================================================================================")
data = response.text

def parse_json(data):
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = parse_json(value)
        else:
            result[key] = value
    return result

# Parsing JSON data using recursion
parsed_data = parse_json(json.loads(data))

#df = pd.json_normalize(json.loads(dataJson))

players = parsed_data["players"]
coaches = parsed_data["coaches"]
dfCoaches = pd.DataFrame(coaches)
dfPlayers = pd.DataFrame(players)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ COACHES +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(dfCoaches.sort_values(by=['position']))   
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ PLAYERS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(dfPlayers.sort_values(by=['name']))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ PLAYER STATS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#get player stats
player_id = '2b6d74b7-10fb-4f17-99c8-9bb557fb475b'
url2 = "https://api.sportradar.com/nfl/official/trial/v7/en/players/"+player_id+"/profile.json?api_key=ndMTecIz2D2DRf1c2xWL46QRx6brsxPM2C0JxhZR"
players_response = requests.get(url2, headers=headers)
data_player = players_response

df_stats = pd.DataFrame(data_player.values(), index=data_player.keys())

print(df_stats)

