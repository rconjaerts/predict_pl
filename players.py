'''
GOTO COMPETITION TOP SCORERS
GET LIST OF PLAYER IDS BY POSITION
GO TO PLAYER ID IN CORRECT SEASON COMPETITION
GET MINUTES PLAYED AND GOALS
'''

import csv
import requests
from time import sleep
from bs4 import BeautifulSoup

ofile  = open('players.csv', "wb")
writer = csv.writer(ofile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE)
writer.writerow(["id", "name", "team_name", "team_id", "position", "goals", "season", "comp_id"])

seasons = {
    2011 : "373",
    2012 : "415",
    2013 : "449",
    2014 : "481",
    2015 : "515"
}

for season in seasons:
    r = requests.get("https://www.statbunker.com/competitions/TopGoalScorers?comp_id="  +str(seasons[season]))
    soup = BeautifulSoup(r.text, 'html.parser')

    rows = soup.find('tbody').find_all('tr')
    for row in rows:
        elem = row.find_all('td')
        name = elem [0].text
        team = elem[1].text
        team_id = elem[1].find('a').get('href')[56:]
        position = row['class'][0]
        goals = elem[2].text
        id = elem[0].find('a').get('href')
        writer.writerow([id, name, team, team_id, position, str(goals), str(season), str(seasons[season])])
    sleep(5)

ofile.close()