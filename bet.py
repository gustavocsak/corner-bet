from scraper import matches_list
import json

START_MINUTES_FIRSTHALF = 38
END_MINUTES_FIRSTHALF = 44

START_MINUTES_SECONDHALF = 83
END_MINUTES_SECONDHALF = 89

MIN_ATTACKS_FIRSTHALF = START_MINUTES_FIRSTHALF
MIN_ATTACKS_SECONDHALF = START_MINUTES_SECONDHALF

CORNER_SHOT_FIRSTHALF = 7
CORNER_SHOT_SECONDHALF = 14

games_to_bet = []

score_difference_list = [0, 1, -1]


for match in matches_list:

    score_difference = match['home_score'] - match['away_score']

    match_timeframe_firsthalf = START_MINUTES_FIRSTHALF <= match['current_minutes'] <= END_MINUTES_FIRSTHALF
    match_timeframe_secondhalf = START_MINUTES_SECONDHALF <= match['current_minutes'] <= END_MINUTES_SECONDHALF

    # Check score difference between teams
    if not (score_difference in score_difference_list):
        continue

    # Check current game live minutes
    if not (match_timeframe_firsthalf or match_timeframe_secondhalf):
        continue

    corner_shot_home = match['home_attack'] + match['home_shot'] + match['home_corner']
    corner_shot_away = match['away_attack'] + match['away_shot'] + match['away_corner']

    # Draw
    if score_difference == 0:

        if match_timeframe_firsthalf:
            if match['home_attack'] >= MIN_ATTACKS_FIRSTHALF or match['away_attack'] >= MIN_ATTACKS_FIRSTHALF:
                if corner_shot_home >= CORNER_SHOT_FIRSTHALF or corner_shot_away >= CORNER_SHOT_FIRSTHALF:
                    games_to_bet.append(match)

        elif match_timeframe_secondhalf:
            if match['home_attack'] >= MIN_ATTACKS_SECONDHALF or match['away_attack'] >= MIN_ATTACKS_SECONDHALF:
                if corner_shot_home >= CORNER_SHOT_FIRSTHALF or corner_shot_away >= CORNER_SHOT_FIRSTHALF:
                    games_to_bet.append(match)

    # Home team winning by one goal
    elif (score_difference == 1):

        if match_timeframe_firsthalf:
            if match['away_attack'] >= MIN_ATTACKS_FIRSTHALF and corner_shot_away >= CORNER_SHOT_FIRSTHALF:
                    games_to_bet.append(match)
        elif match_timeframe_secondhalf:
            if match['away_attack'] >= MIN_ATTACKS_SECONDHALF and corner_shot_away >= CORNER_SHOT_SECONDHALF:
                    games_to_bet.append(match)

    # Away team winning by one goal               
    elif (score_difference == -1):

        if match_timeframe_firsthalf:
            if match['home_attack'] >= MIN_ATTACKS_FIRSTHALF and corner_shot_home >= CORNER_SHOT_FIRSTHALF:
                    games_to_bet.append(match)
        elif match_timeframe_secondhalf:
            if match['home_attack'] >= MIN_ATTACKS_SECONDHALF and corner_shot_home >= CORNER_SHOT_SECONDHALF:
                    games_to_bet.append(match)





for element in games_to_bet:
    print(json.dumps(element, indent=3, default=str))

for element in matches_list:
    print(json.dumps(element, indent=3, default=str))

print('finished')
