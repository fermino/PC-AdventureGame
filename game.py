#!/bin/python

# The game is organized in stages and options inside each one. Each option will take you to the
# defined stage. If a stage has no options, it will be assumed that it is the end of the game.
# There are two special stage names, [START] and [END], and as their names suggest it, the first is
# the entry point and the latter the end. Indentation is just for clarity. 
#
# The format is the following: 

# [STAGE_NAME] {
#   A string of text
#   Something happened! You can [an option:NEXT_STAGE_NAME] or [another option:OTHER_STAGE_NAME]
# }

# Game definition
game = """
[START] {
    You suddenly wake up in the middle of nowhere, you can't remember anything and there's nothing around you to give you a hint of were you came from, you try to remember but nothings comes to your mind. There's a forest close to you, and suddenly you notice that something moves rapidly in the shadows beneath the trees. You are scared, but you can either [run away:RUN] or [investigate:INVESTIGATE].[:DOUBT]
}
[RUN] {
    You stand up as fast as you can and start walking fast. You're almost running. There's something that makes you feel uneasy about this place and you decide to start running. As you do, you notice something shiny a hundred yards away. You start running towards that but you suddenly hear something gigantic behind you. There's no time to lose, you can either look back and [face:FACE] it or try to [escape:ESCAPE].
}
[FACE] {
    You turn back to face whatever that thing is and then you see it. It looks like a man but it's at least 3 times bigger. It has a huge nose and a somewhat destroyed club in one hand. It looks like the typical giant you would see in movies but now that you see it, it's for sure twice as terrifying! He tries to crush you with his feet, and you manage to avoid him a couple of times, but he finally gets to you. You suddenly wake up and realize it was all just a dream...
}
[ESCAPE] {
    You keep running and you happily find out that the giant got quickly distracted with something and is now far behind you. You get to that shiny thing and find out it's a bottle filled with a weird liquid, it is near the edge of a cliff and has a label that says "a trip home". It certainly reminds you of alice in wonderland and you feel ready to take it, but right before you do it someone screams in the distance: "WAIT, WAIT!". You can either [drink:DRINK] it or [wait:WAIT]. 
}
[DRINK] {
    You decide to drink it no matter what, you are actually tired of this whole thing. As you do so, you start feeling sick and dizzy. "NO, IT WAS A TRAP!" screams a girl that just arrives at your side. "Guess she was the voice I heard" you think. She tries to help you but there's not much she can do, as what you took is more powerful than any known antipoison. "Wait, no, no..." She sounds worried and gives you something to drink, and you feel better, but not for long. She tries to explain you that you have a mission to accomplish and something need need your help with, but her voice sounds every time further away, until there's nothing to hear, and nothing to say. 
}
[WAIT] {
    You wait and see a girl running towards you. "DON'T DRINK IT!" She says, taking it from you and making a small scratch in your hand in the intent. She explains you that it was actually poison. As she recovers from the run she explains you that there's an important mission for you to do, but that's up to you to [accept:ACCEPT] it or [decline:DECLINE] it.
}
[ACCEPT] {
    She explains that you need to defy a giant. "It's been disturbing our small community for years. Help us! Will you? I know it might be hard but we don't have any other options. Please..." She sounds worried, and you feel that it's your responsability to help, so you accept it. A couple of fairies appear around you as she explains it. The girl takes a small bottle out of her pocket and explains you that this is not your world, but that they had brought you here through your dreams. "This" She points at the bottle "will take you back to the beggining, but you will not remember anything. Take, just in case" she gives you a flashlight with a slight smile in her face, and then she says: "Are you ready to [go:START]?" She looks at you slightly worried "You can still go [home:HOME] if you want it..."
}
[DECLINE] {
    You decide this is not a risk you're taking today. It still makes you uncomfortable to say no, you feel you should help. "But she looked really worried" you think, trying to reason with yourself, but nothing will make you change your mind. She gives you another bottle to take and as you take it everything becomes blur and vanishes away. "Oh, just a dream" you think as you wake up. But there's something that feels odd, and the tiny scratch in your hand leaves you thinking. "I should've done something better" you say...
}
[INVESTIGATE] {
    Your fear is big but your curiosity is bigger. You stand up and carefully start walking towards the trees. As you approach them you start feeling more and more uneasy until a giant comes out of the trees and tries to crush you with his giant feet! You start running but clearly his legs are a lot longer than yours. You see a tiny space beneath two rocks where you could hide, but you're not sure if you'll fit there. You can either try to [hide:HIDE] or [keep running:KEEP_RUNNING], but before you can decide you see a [firearm:FIGHT] you could use, 20 feet away.
}
[HIDE] {
    You decide to reach those rocks and try to hide beneath them, but as you enter you feel that the floor doesn't support you anymore. You're falling, and as you hit the rock some meters below, you start hearing voices around you. Everything's dark and it's hard to understand them as dizzy as you are after the fall, but you manage to hear "He needs to go back, and he will not remember any of this". "Wait, what? How that I'm not gonna remember this?!" You start feeling scared, but as someone gently touches your head you start falling asleep, starting to wonder how you got there. But now, you need to [wake up:START]. 
}
[KEEP_RUNNING] {
    You make a huge effort to escape, but when you feel that you're getting a bit farther from the giant, you miss a step and everything goes black. When you wake up, you're surrounded by voices, but you still can't see anything. You vaguely remember that you have a flashlight in your pocket, but even if the voices sound friendly, you don't really want to face or see anything else. You can either turn it [on:FLASHLIGHT_ON] or leave it [off:FLASHLIGHT_OFF].
}
[FLASHLIGHT_ON] {
    You turn the flashlight on and what you see makes you feel better. There's around 20 of what you think are fairies surrounding you. They tell you to be relaxed, and that there's nothing to worry about. They explain you that you had been followed by a mountain giant and that they don't really like humans, and later they give you some hot chocolate to drink. They mention that the giants, that one specifically, has been messing around their community for years, and that they'd like you to [hunt:HUNT] him down. But it is up to you, they tell you that if you want, you can go [home:HOME] too. 
}
[HUNT] {
    When you tell them so, they start preparing something for you to drink. They briefly mention that you will remember nothing of this when you wake up. "Wait, WAKE UP?" you say. "AM I DREAMING?". Before anyone responds your question they bring that liquid to you and as your extremely thirsty, you don't think twice. As you start to feel dizzy and sleepy you ask them if you can go home, but they say that it's already too late for that. The only option left is to [go on:START]. 
}
[HOME] {
    A seemingly old fairy gets near to you and start pronouncing some words you can't understand. Everything starts to look weird and funny for a moment, before everything dissapears. You are in your bed. It's 7:00 AM and everything seems to be normal. You get ready for school and while you're having breakfast you notice something in your pocket. It's a flashlight! "When did I put this here?" You say... And then you remember everything... 
    Was it a dream?
}
[FLASHLIGHT_OFF] {
    You decide it's better to keep the flashlight off, at least for now, and as the voices get closer to you, your fear starts to increase. You try to escape and stumble with a couple of rocks in your way, but you manage to get out of there. You hear someone begging you to wait, saying there's danger outside, but all you want to do is get far from this place. When you finally are outside, you see more giants around you. "WHAT ON EARTH?!" you scream, but it's too late to change the course. They're already too close, and as one of them grabs you, you have the slight feeling that this is not the first time you're here...
}
[FIGHT] {
    You make an effort to reach the firearm, and when you finally reach it, it transforms into a sword! "Weird" you think, but honestly it's the only thing you have in hand to help you. You fight and fight and fight, until that giant is finally down. You see more coming, and for some reason you feel you need to face them, so you do. Somehow you have a lot more strength than usual, and as you finish defeating them you see some tiny people (some of them with wings) getting around you. You don't fully understand everything but you feel you've already been there, and as they hug you and cheer you, you feel everything's alright. A girl that looks familiar gives you something "to return home", she says. As you take the small bottle you wonder if you shouldn't [stay:STAY] there, as it felt like if you had already been there for a lot longer than you knew. At the same time you remember your family at home, and feel that you should probably [return:RETURN].
}
[STAY] {
    You decide to stay, and the more time it passes the less you remember the place you came from. You stay with this new people you met, and with time, you end up having a family here. In the end, it feels like nothing could've been different. 
}
[RETURN] {
    You take the bottle and without thinking too much you take it. You wake up, you're home, in your bed. "What time is it?" You say... It's 7:00, and your alarm is ringing. "Guess it was all a dream" you say, but as you try to you realize you can't even recall most of the details. As you get ready for school for some reason you look at your left hand. You see a small scratch that makes you smile, but to be honest, you don't really know the why...
}
[DOUBT] {
    Your have trouble making a decision, and while you try to think a giant comes out of the trees, trying to catch you. You try to run away but it's too late, he reaches you and gets ready to crush you, but right before that happens... You wake up. Luckily, it was just a dream.
}
"""

import re
from colorama import init, Fore

# TODO: Actually implement the distance thing. It doesn't seem to be installed in all systems, though.
init()

# Color definitions
stage_color     = Fore.GREEN
option_color    = Fore.LIGHTRED_EX
choose_color    = Fore.CYAN
error_color     = Fore.RED

# Welcome message :)
print(f"{option_color}Welcome to this game, where you can shape the adventure you'll have. But beware, even when you can choose your path, the game has an objective that YOU must discover. There are different endings, but is up to you to discover The One.")

# Syntax definition
stage_regex     = r"\[([A-Za-z0-9_-]+)\][ \t\r\n]*{([^{}]*)}"
option_regex    = r"\[([^\[\]:]*):([a-zA-Z0-9_.-]+)\]"

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
    user_option = False
    while user_option not in parsed_game[current_stage]['options']:
        user_option = input(f"{choose_color}=> What do you choose? {option_color}").strip().upper()
        # TODO: Implement distance.levenshtein() to handle user typos

    current_stage = parsed_game[current_stage]['options'][user_option]

print(f"{stage_color}- THE END -")
print()