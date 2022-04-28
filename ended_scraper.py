import requests
from bs4 import BeautifulSoup
from db import predictions

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

    if int(element['current_minutes']) < 45:
        corner_result = finished_match.find('td', class_='match_corner').find('div').find('span', class_='span_half_corner').text
        corner_result.replace('(', '').replace(')', '').replace('-', '')
        print(corner_result)
    else:
        corner_result = finished_match.find('td', class_='match_corner').find('div').find('span', class_='span_match_corner').text
        corner_result.replace('-', '').strip()
        print(corner_result)
    


# Check ended table rows based on match id
# When found: check if prediction was made in 1st or 2nd half
# Check corners
# Add to results