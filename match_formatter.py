def match_formatter(match):
    
    possible_errors = ['-', ' -', '- ', ' - ', ' ', '']

    for key in match:
        
        if match[key] in possible_errors:
            match[key] = 0

    if match['current_minutes'] == "Half":
        match['current_minutes'] = 45
        match['half_finished'] = True
    
    elif match['current_minutes'] == "Full":
        match['current_minutes'] = 90
        match['half_finished'] = True
    else:
        match['half_finished'] = False

    for key in match:
        
        if not (key == 'home_team' or key == 'away_team' or key == 'half_finished'):

            match[key] = int(match[key])
    
    return match