import json
import requests
from collections import defaultdict


request = requests.get('https://mach-eight.uc.r.appspot.com/')
response = json.loads(request.text)
players = list(response.values())[0]
spaces = 20
space = ' '

if __name__ == '__main__':

    inch = int(input("> app "))
    players.sort(key=lambda p: int(p['h_in']))
    minimun = int(players[0]['h_in']) + int(players[1]['h_in'])
    maximum = int(players[-1]['h_in']) + int(players[-2]['h_in'])
    if (inch <= maximum) and (inch >= minimun):

        d = defaultdict(list)
        for player in players:
            d[int(player['h_in'])].append(player['first_name'] + " " + player['last_name'])

        for height in d:
            if inch - height in d:
                for other in d[inch - height]:
                    for player in d[height]:
                        if player < other:
                            space_to_print = spaces - len(player)
                            print('- ', player, space_to_print*space, other)
    
    else:
        print(f"No matches found!")
    


