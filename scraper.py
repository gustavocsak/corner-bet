import requests
from bs4 import BeautifulSoup
import json

live_url = 'https://www.totalcorner.com/match/today/'
ended_url = 'https://www.totalcorner.com/match/today/ended'

response = requests.get(live_url)
soup = BeautifulSoup(response.content, 'html.parser')

match_table = soup.find('tbody', class_='tbody_match')
matches = match_table.select('tr')

matches_list = []


possible_errors = ['-', ' -', '- ', ' - ', ' ', '']


for element in matches:

    current_status = element.find('td', class_='match_status').find('span').text

    if(current_status == ''):
        break

    score = element.find('td', class_='match_goal').text
    corners = element.find('td', class_='match_corner').find('div').find('span', class_='span_match_corner').text.replace('-', '').strip()
    attacks = element.find('td', class_='match_attach').find('div', class_='match_dangerous_attacks_div').text.replace('-', '').strip()
    shots = element.find('td', class_='match_shoot').find('div', class_='match_shoot_div').text.replace('-', '').strip()


    match = {
        'home_team': element.find('td', class_='match_home').find('a').text,
        'away_team': element.find('td', class_='match_away').find('a').text,
        'home_score': score[0:1],
        'away_score': score[-1],
        'home_corner': corners[0:2],
        'away_corner': corners[-2],
        'home_attack': attacks[0:2],
        'away_attack': attacks[-2:],
        'home_shots': shots[0:2],
        'away_shots': shots[-2:],
        'current_minutes': current_status

    }

    # Look for a way to convert corners, attacks and shots to integer
    # Values still can be scraped as: '' or ' ' or ' -' or '- '
    # In this case convert it to 0

    matches_list.append(match)


# printing matches in json format:
for element in matches_list:
    print(json.dumps(element, indent=3, default=str))

print('finished')