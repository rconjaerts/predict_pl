# https://www.statbunker.com/players/GetHistoryStats?player_id=32301&comps_type=-1&dates=-1&comps_id=373&clubs_id=-1

import csv
import requests
from time import sleep
from bs4 import BeautifulSoup

wfile  = open('./data/merged_mp.csv', "wb")
rfile  = open('./data/merged.csv', "rb")

reader = csv.reader(rfile, delimiter=';')
writer = csv.writer(wfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE)

rownum = 0

for row in reader:
    if rownum == 0:
        writer.writerow(["season", "team_name", "country", "team_ranking", "competition_points", "id", "name", "team_id", "position", "goals", "comp_id", "age", "minutes_played"])
    elif rownum > 1970:
        player_id = row[5][35:]
        r = requests.get("https://www.statbunker.com/players/GetHistoryStats?comps_type=-1&dates=-1&clubs_id=-1&player_id="+str(player_id)+"&comps_id="+str(row[10]))
        soup = BeautifulSoup(r.text, 'html.parser')

        #print str(rownum)
        #print ("https://www.statbunker.com/players/GetHistoryStats?comps_type=-1&dates=-1&clubs_id=-1&player_id="+str(player_id)+"&comps_id="+str(row[10]))
        
        rows = soup.find('tbody').find_all('tr')
        mp_total = 0
        for row2 in rows:
            mp = row2.find_all('td')[6].text
            if(mp != "-"):
                mp_total += int(mp)
        row.append(str(mp_total))
        writer.writerow(row)

        if rownum % 10 == 0:
            print str(rownum)
            sleep(1)
    
    rownum += 1

wfile.close()
rfile.close()