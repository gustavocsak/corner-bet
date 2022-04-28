def match_formatter(matches):

    formatted_list = []

    for match in matches:

        current_status = match.find('td', class_='match_status').find('span').text

        if(current_status == ''):
            break

        match_id = match['data-match_id']
        home_team = match.find('td', class_='match_home').find('a').text
        away_team = match.find('td', class_='match_away').find('a').text
        score = match.find('td', class_='match_goal').text
        corners = match.find('td', class_='match_corner').find('div').find('span', class_='span_match_corner').text.replace('-', '').strip()
        attacks = match.find('td', class_='match_attach').find('div', class_='match_dangerous_attacks_div').text.replace('-', '').strip()
        shots = match.find('td', class_='match_shoot').find('div', class_='match_shoot_div').text.replace('-', '').strip()

        match = {
            
            'home_team': home_team,
            'away_team': away_team,
            'home_score': score[0:1],
            'away_score': score[-1],
            'home_corner': corners[0:2],
            'away_corner': corners[-2],
            'home_attack': attacks[0:2],
            'away_attack': attacks[-2:],
            'home_shot': shots[0:2],
            'away_shot': shots[-2:],
            'match_id': match_id,
            'current_minutes': current_status

        }

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


        match['corner_sum'] = int(match['home_corner']) + int(match['away_corner'])

        formatted_list.append(match)
        
    
    
    return formatted_list