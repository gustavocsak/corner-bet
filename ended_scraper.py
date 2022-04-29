import requests
from bs4 import BeautifulSoup
from db import predictions, results

ended_url = 'https://www.totalcorner.com/match/today/ended'

response = requests.get(ended_url)
soup = BeautifulSoup(response.content, 'html.parser')

match_table = soup.find('tbody', class_='tbody_match')

matches_list = []

current_predicitons = predictions.find({})

for element in current_predicitons:

    # Find prediction in finished matches table by match id
    finished_match = match_table.find('tr', {"data-match_id": element['match_id']})

    corner_prediction = int(element['home_corner']) + int(element['away_corner'])

    # Check which half bet was placed and get right corner stats
    if int(element['current_minutes']) < 45:
        corner_result = finished_match.find('td', class_='match_corner').find('div').find('span', class_='span_half_corner').text
        corner_result = corner_result.replace('(', '').replace(')', '').replace('-', '')

        corner_sum = int(corner_result[0:1]) + int(corner_result[-1])

    elif int(element['current_minutes']) > 45 and int(element['current_minutes']) < 90:
        corner_result = finished_match.find('td', class_='match_corner').find('div').find('span', class_='span_match_corner').text
        corner_result = corner_result.replace('-', '').strip()

        corner_sum = int(corner_result[0:2]) + int(corner_result[-2])

    if corner_sum > element['corner_sum']:
        element['bet_result'] = 'won'
    else:
        element['bet_result'] = 'lost'

    predictions.delete_one({'_id': element['_id']})

    results.insert_one(element)
