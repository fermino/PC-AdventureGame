#!/bin/python

# Okay, let's first set the game as itself. The program will parse it accordingly, here's an example: 
# The keywords ALWAYS go inside brackets. They're case insensitive. Options are defined by a semicolon before them. The names should be unique. 

# Game definition
game = """
    [START] {
        You suddenly wake up in the middle of nowhere, you can't remember anything and there's
        nothing around you to give you a hint of were you came from, you try to remember but nothings comes
        to your mind. There's a forest close to you, and suddenly you notice that something moves
        rapidly in the shadows beneath the trees. You are scared.
        
        :START_RUN          You quickly stand up and try to run away from it. 
        :START_INVESTIGATE  You face your fears and get ready to face it, whatever it is. 
    }
    [START_RUN] {
        You run asdasdasds
    }
    [START_INVESTIGATE] {
        Your fear is big but your curiosity is bigger. 
    }
"""

import re
from colorama import init, Fore

init()

# Color definitions
stage_color     = Fore.GREEN
option_color    = Fore.CYAN
choose_color    = Fore.LIGHTRED_EX
error_color     = Fore.RED

# Syntax definition
stage_regex     = r"\[([A-Za-z0-9_-]+)\][ \t]*{([^{}]*)}"
option_regex    = r":([^ \t]+)[ \t]?(.*)"
option_char     =  ':'

# Main script
stage_regex = re.compile(stage_regex)
option_regex = re.compile(option_regex)

parsed_game = {}
# For each defined stage, we'll parse the inside lines for text strings and options
for stage in stage_regex.findall(game):
    stage_name = stage[0].upper()

    if stage_name in parsed_game:
        exit(f"{error_color}The stage {stage_name} has been already defined!")

    parsed_game[stage_name] = {
        'text': [],
        'options': {}
    }
    
    # For each line inside the stage, we'll ignore empty lines and parse it according to the defined syntax
    for line in stage[1].split("\n"):
        line = line.strip()
        if line == '':
            continue
        
        # If the line begins with a semicolon, it's an option
        if line[0:1] == option_char:
            option = option_regex.match(line)
            option_name = option[1].upper()
            option_text = option[2].strip()

            parsed_game[stage_name]['options'][option_name] = option_text

            if parsed_game[stage_name]['options'][option_name] == '':
                exit(f"{error_color}The option {parsed_game[stage_name]['options'][option_name]} in stage {stage_name} is missing the text!")
        # If not, it's just text
        else:
            parsed_game[stage_name]['text'].append(line)

# The game :)
current_stage = 'START'

while current_stage != 'END':
    print()

    # If the selected stage is not defined, well, there's not much we can do
    if current_stage not in parsed_game:
        exit(f"{error_color}Stage {current_stage} was not found :C")
    
    # We'll print the text
    for line in parsed_game[current_stage]['text']:
        print(f"{stage_color}{line}")
    print()

    if len(parsed_game[current_stage]['options']) == 0:
        break

    # And the options
    for index, option in enumerate(parsed_game[current_stage]['options'].values(), start=1):
        print(f"{option_color}{index}. {option}")
    print()

    # We'll wait for the user to select an option and we'll switch to the selected stage
    while True:
        user_option = input(f"{choose_color}=> What do you choose? ")
        if user_option.isnumeric():
            user_option = int(user_option)
            if user_option > 0 and user_option <= len(parsed_game[current_stage]['options']):
                current_stage = list(parsed_game[current_stage]['options'])[user_option - 1]
                break

print(f"{stage_color}- THE END -")
print()