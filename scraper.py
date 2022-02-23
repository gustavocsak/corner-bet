from textwrap import indent
import requests
from bs4 import BeautifulSoup
import json

live_url = 'https://www.totalcorner.com/match/today/'
ended_url = 'https://www.totalcorner.com/match/today/ended'

response = requests.get(live_url)

soup = BeautifulSoup(response.content, 'html.parser')

match_table = soup.find("tbody", class_="tbody_match")
matches = match_table.select('tr')

matches_list = []

for element in matches:

    match = {
        'home_team': element.find("td", class_="match_home").find("a").text,
        'away_team': element.find("td", class_="match_away").find("a").text
    }
    matches_list.append(match)


# printing matches in json format:
for element in matches_list:
    print(json.dumps(element, indent=3, default=str))


