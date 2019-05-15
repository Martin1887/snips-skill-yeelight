#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:45:48 2018

@author: martin
"""

import random
import sys

if len(sys.argv) >= 2:
    intent_type = sys.argv[1]

MAX_EXAMPLES = 4000
examples = 0

rooms = []
with open('resources/house_rooms_en.txt', 'rb') as rooms_list:
    for line in rooms_list:
        for room in line.strip().split(', '):
            rooms.append(room)
            
percentages = ['25%', '25 percent', 'the half', 'a quarter', 'an octave',
               '50%', '50 percent', '10%', '10 percent', '20%',
               '20 percent', '10%', '10 percent', '15%', '15 percent',
               '40%', '40 percent', '30%', '30 percent']

colors = ['white', 'gray', 'grey', 'magenta', 'fucsia', 'purple',
          'salmon', 'orange', 'yellow','olive', 'golden', 'red',
          'dark red', 'green', 'dark green', 'lime', 'brown', 'blue', 'indigo',
          'dark blue', 'cyan', 'light blue', 'azure', 'sky-blue',
          'aquamarine', 'cobalt', 'turquoise']

temperatures = range(1700, 6500, 250)

# Positive and negative words
UP = ['Rise', 'Up', 'Increase']
up = ['rise', 'up', 'increase']
DOWN = ['Down', 'Reduce']
down = ['down', 'reduce']
WISH = ['I want', 'I need', 'I would like', 'I wish']
wish = ['I want', 'I need', 'I would like', 'I wish']
light = ['light', 'light intensity', 'bright', 'brightness']
dark = ['dim light', 'dark']

if intent_type == 'changeTemperature':
    for t in temperatures:
        print 'Color temperature at [{}](temperature)'.format(t)
        for w in WISH:
            print '{} color temperature at [{}](temperature)'.format(w, t)
        for room in rooms:
            print 'Color temperature at [{}](temperature) in the [{}](house_room)'.format(t, room)
            for w in WISH:
                print '{} color temperature at [{}](temperature) in the [{}](house_room)'.format(w, t, room)

if intent_type in ['increaseTemperature', 'reduceTemperature']:
    if intent_type == 'increaseTemperature':
        print 'More color temperature'
        print 'Warmer color temperature'
        print 'Warmer light'
        examples += 3
    else:
        print 'Less color temperature'
        print 'Colder color temperature'
        print 'Cooler color temperature'
        print 'Colder light'
        print 'Cooler light'
        examples += 5
    

    if intent_type == 'increaseTemperature':
        factor = UP
    else:
        factor = DOWN
        for perc in percentages:
            for w in WISH:
                print '{} color temperature by [{}](percent)'.format(w, perc)
                examples += 1
                
    for perc in percentages:
        for f in factor:
            print '{} color temperature by [{}](percent)'.format(f, perc)
            examples += 1
        for w in WISH:
            print '{} [{}](percent) more of color temperatuer'.format(w, perc)
            examples += 1
        
    for room in rooms:
        for f in factor:
            print '{} color temperature by [{}](percent)'.format(f, perc)
            examples += 1
        for w in WISH:
            print '{} [{}](percent) of color temperature'.format(w, perc)
            examples += 1
    
    while examples < MAX_EXAMPLES - 25:
        perc = random.choice(percentages)
        room = random.choice(rooms)
        l = 'color temperature'
        f = random.choice(UP)
        w = random.choice(WISH)
        print '{} {} by [{}](percent) in the [{}](house_room)'.format(f, l, perc, room)
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)
        print '{} {} in the [{}](house_room) by [{}](percent)'.format(f, l, room, perc)
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(up)
        w = random.choice(WISH)
        print 'In the [{}](house_room) {} {} by [{}](percent)'.format(room, f, l, perc)
        
        examples += 3
        
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)    
        print '{} [{}](percent) more of {} in the [{}](house_room)'.format(w, perc, l, room)
        erc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(wish)    
        print 'In the [{}](house_room) {} [{}](percent) more of {}'.format(room, w, perc, l)
        examples += 2
        
        if intent_type != 'increaseTemperature':
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
        
            print '{} {} by [{}](percent) in the [{}](house_room)'.format(f, l, perc, room)
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            print '{} {} in the [{}](house_room) by [{}](percent)'.format(f, l, room, perc)
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(down)
            w = random.choice(WISH)
            print 'In the [{}](house_room) {} {} by [{}](percent)'.format(room, f, l, perc)
            
            examples += 3
            
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            print '{} [{}](percent) less of {} by [{}](house_room)'.format(w, perc, l, room)
            erc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(wish)
            print 'In the [{}](house_room) {} [{}](percent) less of {}'.format(room, w, perc, l)
            examples += 2

if intent_type == 'changeBrightness':
    for perc in percentages:
        for l in light:
            for f in ['Put', 'Set', 'Change']:
                print '{} {} at [{}](percent)'.format(f, l, perc)
            for w in WISH:
                print '{} a [{}](percent) of {}'.format(w, perc, l)
                print '{} [{}](percent) of {}'.format(w, perc, l)
            for room in rooms:
                if random.randint(0, len(rooms)) < 1:
                    for f in ['Put', 'Set', 'Change']:
                        if random.randint(0, 3) < 1:
                            print '{} {} at [{}](percent) in the [{}](house_room)'.format(f, l, perc, room)
                            print '{} {} in the [{}](house_room) at [{}](percent)'.format(f, l, room, perc)
                    for w in WISH:
                        if random.randint(0, len(WISH)) < 1:
                            print '{} a [{}](percent) of {} int he [{}](house_room)'.format(w, perc, l, room)
                            print '{} a [{}](percent) in the [{}](house_room) of {}'.format(w, perc, room, l)
                            print '{} [{}](percent) of {} in the [{}](house_room)'.format(w, perc, l, room)
                            print '{} [{}](percent) in the [{}](house_room) of {}'.format(w, perc, room, l)
                            print '{} el [{}](percent) of {} in the [{}](house_room)'.format(w, perc, l, room)
                            print '{} el [{}](percent) in the [{}](house_room) of {}'.format(w, perc, room, l)

if intent_type == 'changeColor':
    for c in colors:
        print 'Put the color [{}](color)'.format(c)
        print 'Change the color to [{}](color)'.format(c)
        print 'Change light to [{}](color)'.format(c)
        print 'Put light [{}](color)'.format(c)
        print 'Put light at color [{}](color)'.format(c)
        print 'Light [{}](color)'.format(c)
        print 'Light of color [{}](color)'.format(c)
        for w in WISH:
            print '{} change the color to [{}](color)'.format(w, c)
            print '{} change the light to [{}](color)'.format(w, c)
            print '{} change the light to the color [{}](color)'.format(w, c)
            print '{} put color [{}](color)'.format(w, c)
            print '{} light [{}](color)'.format(w, c)
            print '{} light at color [{}](color)'.format(w, c)

        if random.randint(0, len(colors)) < 2:
            for room in rooms:
                if random.randint(0, len(rooms)) < 15:
                    print 'Put color [{}](color) in the [{}](house_room)'.format(c, room)
                    print 'Change the color to [{}](color) in the [{}](house_room)'.format(c, room)
                    print 'Change the light to [{}](color) in the [{}](house_room)'.format(c, room)
                    print 'Put light [{}](color) in the [{}](house_room)'.format(c, room)
                    print 'Put light at color [{}](color) in the [{}](house_room)'.format(c, room)
                    print 'Light [{}](color) in the [{}](house_room)'.format(c, room)
                    print 'Light at color [{}](color) in the [{}](house_room)'.format(c, room)
                    for w in WISH:
                        if random.randint(0, len(WISH)) < 1:
                            print '{} change the color to [{}](color) in the [{}](house_room)'.format(w, c, room)
                            print '{} change light at [{}](color) in the [{}](house_room)'.format(w, c, room)
                            print '{} change light at color [{}](color) in the [{}](house_room)'.format(w, c, room)
                            print '{} put color [{}](color) in the [{}](house_room)'.format(w, c, room)
                            print '{} light [{}](color) in the [{}](house_room)'.format(w, c, room)
                            print '{} light at color [{}](color) in the [{}](house_room)'.format(w, c, room)

if intent_type in ['turnOn', 'turnOff']:
    if intent_type == 'turnOn':
        print 'Turn on light'
        print 'Turn on lights'
        print 'Switch on light'
        print 'Switch on lights'
        for w in WISH:
            print '{} light'.format(w)
            print '{} turn on light'.format(w)
            print '{} turn on lights'.format(w)
            print '{} switch on light'.format(w)
            print '{} switch on lights'.format(w)
    else:
        print 'Turn off light'
        print 'Turn off lights'
        print 'Switch off light'
        print 'Switch off lights'
        for w in WISH:
            print '{} turn off light'.format(w)
            print '{} turn off lights'.format(w)
            print '{} switch off light'.format(w)
            print '{} switch off lights'.format(w)

    for room in rooms:
        if intent_type == 'turnOn':
            print 'Turn on light in the [{}](house_room)'.format(room)
            print 'Turn on lights in the [{}](house_room)'.format(room)
            print 'Switch on light in the [{}](house_room)'.format(room)
            print 'Switch on lights in the [{}](house_room)'.format(room)
            for w in WISH:
                print '{} light in the [{}](house_room)'.format(w, room)
                print '{} turn on light in the [{}](house_room)'.format(w, room)
                print '{} turn on lights in the [{}](house_room)'.format(w, room)
                print '{} switch on light in the [{}](house_room)'.format(w, room)
                print '{} switch on lights in the [{}](house_room)'.format(w, room)
        else:
            print 'Turn off light in the [{}](house_room)'.format(room)
            print 'Turn off lights in the [{}](house_room)'.format(room)
            print 'Switch off light in the [{}](house_room)'.format(room)
            print 'Switch off lights in the [{}](house_room)'.format(room)
            for w in WISH:
                print '{} turn off light in the [{}](house_room)'.format(w, room)
                print '{} turn off lights in the [{}](house_room)'.format(w, room)
                print '{} switch off light in the [{}](house_room)'.format(w, room)
                print '{} switch off lights in the [{}](house_room)'.format(w, room)

if intent_type in ['increaseBrightness', 'reduceBrightness']:

    if intent_type == 'increaseBrightness':
        print 'I cannot see'
        print 'I can\'t see'
        for l in light:
            print 'Not enough {}'.format(l)
            print 'I need more {}'.format(l)
            print 'There is low {}'.format(l)
            print 'I want more {}'.format(l)
            print 'I would like more {}'.format(l)
            print 'I wish more {}'.format(l)
            print 'More {}'.format(l)
        examples += 30
    else:
        print 'Too much light'
        print 'I want less light'
        print 'I need less light'
        print 'I wish less light'
        print 'I would like less light'
        print 'I want dimmer light'
        print 'I need dimmer light'
        print 'I would like dimmer light'
        print 'I wish dimmer light'
        print 'I want more darkness'
        print 'I need more darkness'
        print 'I wish more darkenss'
        print 'I would like more darkness'
        print 'More darkness'
        examples += 14
    

    if intent_type == 'increaseBrightness':
        factor = UP
    else:
        factor = DOWN
        for perc in percentages:
            for w in WISH:
                print '{} [{}](percent) more of darkness'.format(w, perc)
                examples += 1
                
    for perc in percentages:
        for l in light:
            for f in factor:
                print '{} {} by [{}](percent)'.format(f, l, perc)
                examples += 2
            for w in WISH:
                print '{} [{}](percent) more of {}'.format(w, perc, l)
                examples += 1
        
    for room in rooms:
        if intent_type == 'increaseBrightness':
            print 'I cannot see in the [{}](house_room)'.format(room)
            print 'I can\'t see in the [{}](house_room)'.format(room)
            examples += 2
        else:
            for w in WISH:
                print '{} more darkness in the [{}](house_room)'.format(w, room)
                print '{} dimmer light in the [{}](house_room)'.format(w, room)
                examples += 2
                
        for l in light:
            if intent_type == 'increaseBrightness':
                print 'Not enough light in the [{}](house_room)'.format(room)
                print 'More light in the [{}](house_room)'.format(room)
                print 'Too much darkness in the [{}](house_room)'.format(room)
                examples += 3
                for w in WISH:
                    print '{} more {} in the [{}](house_room)'.format(w, l, room)
                    examples += 1
            else:            
                print 'Too much {} in the [{}](house_room)'.format(l, room)
                examples += 1
    
    while examples < MAX_EXAMPLES - 25:
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)
        if intent_type == 'increaseBrightness':
            l = random.choice(light)
        else:
            l = 'darkness'
        print '{} {} by [{}](percent) in the [{}](house_room)'.format(f, l, perc, room)
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)
        if intent_type == 'increaseBrightness':
            l = random.choice(light)
        else:
            l = 'darkness'
        print '{} {} in the [{}](house_room) by [{}](percent)'.format(f, l, room, perc)
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(up)
        w = random.choice(WISH)
        if intent_type == 'increaseBrightness':
            l = random.choice(light)
        else:
            l = 'darkness'       
        print 'In the [{}](house_room) {} {} by [{}](percent)'.format(room, f, l, perc)
        
        examples += 3
        
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)
        if intent_type == 'increaseBrightness':
            l = random.choice(light)
        else:
            l = 'darkness'        
        print '{} [{}](percent) more of {} in the [{}](house_room)'.format(w, perc, l, room)
        erc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(wish)
        if intent_type == 'increaseBrightness':
            l = random.choice(light)
        else:
            l = 'darkness'        
        print 'In the [{}](house_room) {} [{}](percent) more of {}'.format(room, w, perc, l)
        examples += 2
        
        if intent_type != 'increaseBrightness':
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            l = random.choice(light)
        
            print '{} {} by [{}](percent) in the [{}](house_room)'.format(f, l, perc, room)
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            l = random.choice(light)
            print '{} {} in the [{}](house_room) by [{}](percent)'.format(f, l, room, perc)
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(down)
            w = random.choice(WISH)
            l = random.choice(light)
            print 'In the [{}](house_room) {} {} by [{}](percent)'.format(room, f, l, perc)
            
            examples += 3
            
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            l = random.choice(light)
            print '{} [{}](percent) less of {} in the [{}](house_room)'.format(w, perc, l, room)
            erc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(wish)
            l = random.choice(light)
            print 'In the [{}](house_room) {} [{}](percent) less of {}'.format(room, w, perc, l)
            examples += 2
