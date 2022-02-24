def match_formatter(match):

    
    possible_errors = ['-', ' -', '- ', ' - ', ' ', '']

    # First convert empty spaces or non-numeric strings to 0
    if(match['away_corner'] in possible_errors):
        match['away_corner'] = 0
    
    if(match['home_corner'] in possible_errors):
        match['home_corner'] = 0
    
    if(match['away_attack'] in possible_errors):
        match['away_attack'] = 0
    
    if(match['home_attack'] in possible_errors):
        match['home_attack'] = 0
    
    if(match['away_shot'] in possible_errors):
        match['away_shot'] = 0

    if(match['home_shot'] in possible_errors):
        match['home_shot'] = 0

    if(match['current_minutes'] == "Half"):
        match['current_minutes'] = 45
        match['half_finished'] = True
    else:
        match['half_finished'] = False

    if(match['current_minutes'] == "Full"):
        match['current_minutes'] = 90
        match['half_finished'] = True
    else:
        match['half_finished'] = False

    for key in match:
        
        if not (key == 'home_team' or key == 'away_team' or key == 'half_finished'):

            match[key] = int(match[key])
    
    return match

