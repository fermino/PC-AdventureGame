#!/bin/python

# The game is organized in stages and options inside each one. Each option will take you to the
# defined stage. If a stage has no options, it will be assumed that it is the end of the game.
# There are two special stage names, [START] and [END], and as their names suggest it, the first is
# the entry point and the latter the end. 
#
# The format is the following: 

# [STAGE_NAME] {
#   A string of text
#   Something happened! You can [an option:NEXT_STAGE_NAME] or [another option:OTHER_STAGE_NAME]
# }

# Game definition
game = """
    [START] {
        You suddenly wake up in the middle of nowhere, you can't remember anything and there's
        nothing around you to give you a hint of were you came from, you try to remember but nothings comes
        to your mind. There's a forest close to you, and suddenly you notice that something moves
        rapidly in the shadows beneath the trees. You are scared, but you can either [run:START_RUN] away or [investigate:START_INVESTIGATE].
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
option_color    = Fore.LIGHTRED_EX
choose_color    = Fore.CYAN
error_color     = Fore.RED

# Syntax definition
stage_regex     = r"\[([A-Za-z0-9_-]+)\][ \t\r\n]*{([^{}]*)}"
option_regex    = r"\[([^\[\]:]+):([a-zA-Z0-9_.-]+)\]"

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
        
        # For every choice we find we'll add it to the parsed game and update the string accordingly
        for option in option_regex.findall(line):
            option_name = option[1].upper()
            option_text = option[0].strip().upper()

            parsed_game[stage_name]['options'][option_text] = option_name

            if parsed_game[stage_name]['options'][option_text] == '':
                exit(f"{error_color}The option {parsed_game[stage_name]['options'][option_text]} in stage {stage_name} is missing the text!")
            
            line = line.replace(f"[{option[0]}:{option[1]}]", f"{option_color}{option_text}{stage_color}")
        
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

    # We'll wait for the user to select an option and we'll switch to the selected stage
    user_option = ''
    while user_option not in parsed_game[current_stage]['options']:
        user_option = input(f"{choose_color}=> What do you choose? {option_color}").strip().upper()
        # TODO: Implement distance.levenshtein() to handle user typos

    current_stage = parsed_game[current_stage]['options'][user_option]

print(f"{stage_color}- THE END -")
print()