import requests
from bs4 import BeautifulSoup
from match_formatter import match_formatter
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


# Get predictions
# Check ended table rows based on team names
# When found: check if prediction was made in 1st or 2nd half
# Check corners
# Add to results