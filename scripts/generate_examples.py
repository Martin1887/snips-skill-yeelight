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
with open('resources/house_rooms.txt', 'rb') as rooms_list:
    for line in rooms_list:
        for room in line.strip().split(', '):
            rooms.append(room)
            
percentages = ['25%', '25 por ciento', 'la mitad', 'un cuarto', 'un octavo',
               '50%', '50 por ciento', '10%', '10 por ciento', '20%',
               '20 por ciento', '10%', '10 por ciento', '15%', '15 por ciento',
               '40%', '40 por ciento', '30%', '30 por ciento']

colors = ['blanco', 'blanca', 'gris', 'magenta', 'fucsia', 'morado', 'morada',
          'púrpura', 'violeta', 'salmón', 'naranja', 'amarillo', 'amarilla',
          'oliva', 'dorado', 'dorada', 'gualdo', 'gualda', 'rojo', 'roja',
          'granate', 'rojo oscuro', 'roja oscura', 'verde', 'verde oscuro',
          'verde oscura', 'lima', 'marrón', 'ocre', 'azul', 'añil',
          'azul oscuro', 'cian', 'azul claro', 'azul clara', 'azul cielo',
          'aguamarina', 'celeste', 'cobalto', 'turquesa']

temperatures = range(1700, 6500, 250)

# Positive and negative words
UP = ['Sube', 'Aumenta']
up = ['sube', 'aumenta']
DOWN = ['Baja', 'Reduce', 'Disminuye']
down = ['baja', 'reduce', 'disminuye']
WISH = ['Quiero', 'Necesito', 'Me gustaría tener', 'Deseo']
wish = ['quiero', 'necesito', 'me gustaría tener', 'deseo']
light = ['luz', 'intensidad de luz', 'brillo', 'claridad', 'luminosidad']
dark = ['luz tenue', 'oscuridad']

if intent_type == 'cambiarTemperatura':
    for t in temperatures:
        print 'Temperatura de color de [{}](temperature)'.format(t)
        for w in WISH:
            print '{} una temperatura de color de [{}](temperature)'.format(w, t)
        for room in rooms:
            print 'Temperatura de color de [{}](temperature) en [{}](house_room)'.format(t, room)
            for w in WISH:
                print '{} una temperatura de color de [{}](temperature) en [{}](house_room)'.format(w, t, room)

if intent_type in ['aumentarTemperatura', 'reducirTemperatura']:
    if intent_type == 'aumentarTemperatura':
        print 'Más temperatura de color'
        print 'Temperatura de color más calida'
        print 'Luz más cálida'
        examples += 3
    else:
        print 'Menos temperatura de color'
        print 'Temperatura de color más fría'
        print 'Luz más fría'
        examples += 3
    

    if intent_type == 'aumentarTemperatura':
        factor = UP
    else:
        factor = DOWN
        for perc in percentages:
            for w in WISH:
                print '{} la temperatura de color un [{}](percent)'.format(w, perc)
                examples += 1
                
    for perc in percentages:
        for f in factor:
            print '{} la temperatura de color en un [{}](percent)'.format(f, perc)
            examples += 1
        for w in WISH:
            print '{} [{}](percent) más de temperatura de color'.format(w, perc)
            examples += 1
        
    for room in rooms:
        for f in factor:
            print '{} la temperatura de color en un [{}](percent)'.format(f, perc)
            examples += 1
        for w in WISH:
            print '{} [{}](percent) más de temperatura de color'.format(w, perc)
            examples += 1
    
    while examples < MAX_EXAMPLES - 25:
        perc = random.choice(percentages)
        room = random.choice(rooms)
        l = 'temperatura de color'
        f = random.choice(UP)
        w = random.choice(WISH)
        print '{} la {} en un [{}](percent) en el [{}](house_room)'.format(f, l, perc, room)
        print '{} la {} en un [{}](percent) en la [{}](house_room)'.format(f, l, perc, room)
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)
        print '{} la {} en el [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
        print '{} la {} en la [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(up)
        w = random.choice(WISH)
        print 'En el [{}](house_room) {} la {} en un [{}](percent)'.format(room, f, l, perc)
        print 'En la [{}](house_room) {} la {} en un [{}](percent)'.format(room, f, l, perc)
        
        examples += 6
        
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)    
        print '{} [{}](percent) más de {} en la [{}](house_room)'.format(w, perc, l, room)
        erc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(wish)    
        print 'En el [{}](house_room) {} [{}](percent) más de {}'.format(room, w, perc, l)
        print 'En la [{}](house_room) {} [{}](percent) más de {}'.format(room, w, perc, l)
        examples += 3
        
        if intent_type != 'aumentarTemperatura':
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
        
            print '{} la {} en un [{}](percent) en el [{}](house_room)'.format(f, l, perc, room)
            print '{} la {} en un [{}](percent) en la [{}](house_room)'.format(f, l, perc, room)
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            print '{} la {} en el [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
            print '{} la {} en la [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(down)
            w = random.choice(WISH)
            print 'En el [{}](house_room) {} la {} en un [{}](percent)'.format(room, f, l, perc)
            print 'En la [{}](house_room) {} la {} en un [{}](percent)'.format(room, f, l, perc)
            
            examples += 6
            
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            print '{} [{}](percent) menos de {} en el [{}](house_room)'.format(w, perc, l, room)
            print '{} [{}](percent) menos de {} en la [{}](house_room)'.format(w, perc, l, room)
            erc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(wish)
            print 'En el [{}](house_room) {} [{}](percent) menos de {}'.format(room, w, perc, l)
            print 'En la [{}](house_room) {} [{}](percent) menos de {}'.format(room, w, perc, l)
            examples += 4

if intent_type == 'cambiarBrillo':
    for perc in percentages:
        for l in light:
            for f in ['Pon', 'Establece', 'Cambia']:
                print '{} la {} a un [{}](percent)'.format(f, l, perc)
                print '{} el {} a un [{}](percent)'.format(f, l, perc)
                print '{} la {} a [{}](percent)'.format(f, l, perc)
                print '{} el {} a [{}](percent)'.format(f, l, perc)
                print '{} la {} al [{}](percent)'.format(f, l, perc)
                print '{} el {} al [{}](percent)'.format(f, l, perc)
            for w in WISH:
                print '{} un [{}](percent) de {}'.format(w, perc, l)
                print '{} [{}](percent) de {}'.format(w, perc, l)
                print '{} el [{}](percent) de {}'.format(w, perc, l)
            for room in rooms:
                if random.randint(0, len(rooms)) < 1:
                    for f in ['Pon', 'Establece', 'Cambia']:
                        if random.randint(0, 3) < 1:
                            print '{} la {} a un [{}](percent) en el [{}](house_room)'.format(f, l, perc, room)
                            print '{} la {} a un [{}](percent) en la [{}](house_room)'.format(f, l, perc, room)
                            print '{} la {} a [{}](percent) en el [{}](house_room)'.format(f, l, perc, room)
                            print '{} la {} a [{}](percent) en la [{}](house_room)'.format(f, l, perc, room)
                            print '{} la {} al [{}](percent) en el [{}](house_room)'.format(f, l, perc, room)
                            print '{} la {} al [{}](percent) en la [{}](house_room)'.format(f, l, perc, room)
                            print '{} la {} en el [{}](house_room) a un [{}](percent)'.format(f, l, room, perc)
                            print '{} la {} en la [{}](house_room) a un [{}](percent)'.format(f, l, room, perc)
                            print '{} la {} en el [{}](house_room) a [{}](percent)'.format(f, l, room, perc)
                            print '{} la {} en la [{}](house_room) a [{}](percent)'.format(f, l, room, perc)
                            print '{} la {} en el [{}](house_room) al [{}](percent)'.format(f, l, room, perc)
                            print '{} la {} en la [{}](house_room) al [{}](percent)'.format(f, l, room, perc)
                    for w in WISH:
                        if random.randint(0, len(WISH)) < 1:
                            print '{} un [{}](percent) de {} en el [{}](house_room)'.format(w, perc, l, room)
                            print '{} un [{}](percent) de {} en la [{}](house_room)'.format(w, perc, l, room)
                            print '{} un [{}](percent) en el [{}](house_room) de {}'.format(w, perc, room, l)
                            print '{} un [{}](percent) en la [{}](house_room) de {}'.format(w, perc, room, l)
                            print '{} [{}](percent) de {} en el [{}](house_room)'.format(w, perc, l, room)
                            print '{} [{}](percent) de {} en la [{}](house_room)'.format(w, perc, l, room)
                            print '{} [{}](percent) en el [{}](house_room) de {}'.format(w, perc, room, l)
                            print '{} [{}](percent) en la [{}](house_room) de {}'.format(w, perc, room, l)
                            print '{} el [{}](percent) de {} en el [{}](house_room)'.format(w, perc, l, room)
                            print '{} el [{}](percent) de {} en la [{}](house_room)'.format(w, perc, l, room)
                            print '{} el [{}](percent) en el [{}](house_room) de {}'.format(w, perc, room, l)
                            print '{} el [{}](percent) en la [{}](house_room) de {}'.format(w, perc, room, l)

if intent_type == 'cambiarColor':
    for c in colors:
        print 'Pon color [{}](color)'.format(c)
        print 'Cambia el color a [{}](color)'.format(c)
        print 'Cambia la luz a [{}](color)'.format(c)
        print 'Pon luz [{}](color)'.format(c)
        print 'Pon luz de color [{}](color)'.format(c)
        print 'Luz [{}](color)'.format(c)
        print 'Luz de color [{}](color)'.format(c)
        for w in WISH:
            print '{} cambiar el color a [{}](color)'.format(w, c)
            print '{} cambiar la luz a [{}](color)'.format(w, c)
            print '{} cambiar la luz al color [{}](color)'.format(w, c)
            print '{} poner color [{}](color)'.format(w, c)
            print '{} luz [{}](color)'.format(w, c)
            print '{} luz de color [{}](color)'.format(w, c)

        if random.randint(0, len(colors)) < 2:
            for room in rooms:
                if random.randint(0, len(rooms)) < 15:
                    print 'Pon color [{}](color) en el [{}](house_room)'.format(c, room)
                    print 'Pon color [{}](color) en la [{}](house_room)'.format(c, room)
                    print 'Cambia el color a [{}](color) en el [{}](house_room)'.format(c, room)
                    print 'Cambia el color a [{}](color) en la [{}](house_room)'.format(c, room)
                    print 'Cambia la luz a [{}](color) en el [{}](house_room)'.format(c, room)
                    print 'Cambia la luz a [{}](color) en la [{}](house_room)'.format(c, room)
                    print 'Pon luz [{}](color) en el [{}](house_room)'.format(c, room)
                    print 'Pon luz [{}](color) en la [{}](house_room)'.format(c, room)
                    print 'Pon luz de color [{}](color) en el [{}](house_room)'.format(c, room)
                    print 'Pon luz de color [{}](color) en la [{}](house_room)'.format(c, room)
                    print 'Luz [{}](color) en el [{}](house_room)'.format(c, room)
                    print 'Luz [{}](color) en la [{}](house_room)'.format(c, room)
                    print 'Luz de color [{}](color) en el [{}](house_room)'.format(c, room)
                    print 'Luz de color [{}](color) en la [{}](house_room)'.format(c, room)
                    for w in WISH:
                        if random.randint(0, len(WISH)) < 1:
                            print '{} cambiar el color a [{}](color) en el [{}](house_room)'.format(w, c, room)
                            print '{} cambiar el color a [{}](color) en la [{}](house_room)'.format(w, c, room)
                            print '{} cambiar la luz a [{}](color) en el [{}](house_room)'.format(w, c, room)
                            print '{} cambiar la luz a [{}](color) en la [{}](house_room)'.format(w, c, room)
                            print '{} cambiar la luz al color [{}](color) en el [{}](house_room)'.format(w, c, room)
                            print '{} cambiar la luz al color [{}](color) en la [{}](house_room)'.format(w, c, room)
                            print '{} poner color [{}](color) en el [{}](house_room)'.format(w, c, room)
                            print '{} poner color [{}](color) en la [{}](house_room)'.format(w, c, room)
                            print '{} luz [{}](color) en el [{}](house_room)'.format(w, c, room)
                            print '{} luz [{}](color) en la [{}](house_room)'.format(w, c, room)
                            print '{} luz de color [{}](color) en el [{}](house_room)'.format(w, c, room)
                            print '{} luz de color [{}](color) en la [{}](house_room)'.format(w, c, room)

if intent_type in ['encender', 'apagar']:
    if intent_type == 'encender':
        print 'Enciende la luz'
        print 'Enciende las luces'
        print 'Da la luz'
        print 'Da las luces'
        print 'Prende la luz'
        print 'Prende las luces'
        for w in WISH:
            print '{} luz'.format(w)
            print '{} encender la luz'.format(w)
            print '{} encender las luces'.format(w)
            print '{} prender la luz'.format(w)
            print '{} prender las luces'.format(w)
            print '{} dar la luz'.format(w)
            print '{} dar las luces'.format(w)
    else:
        print 'Apaga la luz'
        print 'Apaga las luces'
        print 'Quita la luz'
        print 'Quita las luces'
        for w in WISH:
            print '{} apagar la luz'.format(w)
            print '{} apagar las luces'.format(w)
            print '{} quitar la luz'.format(w)
            print '{} quitar las luces'.format(w)

    for room in rooms:
        if intent_type == 'encender':
            print 'Enciende la luz en el [{}](house_room)'.format(room)
            print 'Enciende la luz en la [{}](house_room)'.format(room)
            print 'Enciende las luces en el [{}](house_room)'.format(room)
            print 'Enciende las luces en la [{}](house_room)'.format(room)
            print 'Da la luz en el [{}](house_room)'.format(room)
            print 'Da la luz en la [{}](house_room)'.format(room)
            print 'Da las luces en el [{}](house_room)'.format(room)
            print 'Da las luces en la [{}](house_room)'.format(room)
            print 'Prende la luz en el [{}](house_room)'.format(room)
            print 'Prende la luz en la [{}](house_room)'.format(room)
            print 'Prende las luces en el [{}](house_room)'.format(room)
            print 'Prende las luces en la [{}](house_room)'.format(room)
            for w in WISH:
                print '{} luz en el [{}](house_room)'.format(w, room)
                print '{} luz en la [{}](house_room)'.format(w, room)
                print '{} encender la luz en el [{}](house_room)'.format(w, room)
                print '{} encender la luz en la [{}](house_room)'.format(w, room)
                print '{} encender las luces en el [{}](house_room)'.format(w, room)                
                print '{} encender las luces en la [{}](house_room)'.format(w, room)
                print '{} prender la luz en el [{}](house_room)'.format(w, room)
                print '{} prender la luz en la [{}](house_room)'.format(w, room)
                print '{} prender las luces en el [{}](house_room)'.format(w, room)                
                print '{} prender las luces en la [{}](house_room)'.format(w, room)
                print '{} dar la luz en el [{}](house_room)'.format(w, room)
                print '{} dar la luz en la [{}](house_room)'.format(w, room)
                print '{} dar las luces en el [{}](house_room)'.format(w, room)                
                print '{} dar las luces en la [{}](house_room)'.format(w, room)
        else:
            print 'Apaga la luz en el [{}](house_room)'.format(room)
            print 'Apaga la luz en la [{}](house_room)'.format(room)
            print 'Apaga las luces en el [{}](house_room)'.format(room)
            print 'Apaga las luces en la [{}](house_room)'.format(room)
            print 'Quita la luz en el [{}](house_room)'.format(room)
            print 'Quita la luz en la [{}](house_room)'.format(room)
            print 'Quita las luces en el [{}](house_room)'.format(room)
            print 'Quita las luces en la [{}](house_room)'.format(room)
            for w in WISH:
                print '{} apagar la luz en el [{}](house_room)'.format(w, room)
                print '{} apagar la luz en la [{}](house_room)'.format(w, room)
                print '{} apagar las luces en el [{}](house_room)'.format(w, room)
                print '{} apagar las luces en la [{}](house_room)'.format(w, room)
                print '{} quitar la luz en el [{}](house_room)'.format(w, room)
                print '{} quitar la luz en la [{}](house_room)'.format(w, room)
                print '{} quitar las luces en el [{}](house_room)'.format(w, room)
                print '{} quitar las luces en la [{}](house_room)'.format(w, room)

if intent_type in ['aumentarBrillo', 'reducirBrillo']:

    if intent_type == 'aumentarBrillo':
        print 'No veo'
        print 'Sigo sin ver'
        print 'Continúo sin ver'
        for l in light:
            print 'No hay suficiente {}'.format(l)
            print 'Necesito más {}'.format(l)
            print 'Hay muy poca {}'.format(l)
            print 'Quiero más {}'.format(l)
            print 'Me gustaría tener más {}'.format(l)
            print 'Deseo más {}'.format(l)
            print 'Más {}'.format(l)
        examples += 31
    else:
        print 'Demasiada luz'
        print 'Quiero menos luz'
        print 'Necesito menos luz'
        print 'Deseo menos luz'
        print 'Me gustaría tener menos luz'
        print 'Quiero luz más tenue'
        print 'Necesito luz más tenue'
        print 'Me gustaría una luz más tenue'
        print 'Deseo una luz más tenue'
        print 'Quiero más oscuridad'
        print 'Necesito más oscuridad'
        print 'Deseo más oscuridad'
        print 'Me gustaría tener más oscuridad'
        print 'Más oscuridad'
        examples += 14
    

    if intent_type == 'aumentarBrillo':
        factor = UP
    else:
        factor = DOWN
        for perc in percentages:
            for w in WISH:
                print '{} [{}](percent) más de oscuridad'.format(w, perc)
                examples += 1
                
    for perc in percentages:
        for l in light:
            for f in factor:
                print '{} la {} en un [{}](percent)'.format(f, l, perc)
                print '{} el {} en un [{}](percent)'.format(f, l, perc)
                examples += 2
            for w in WISH:
                print '{} [{}](percent) más de {}'.format(w, perc, l)
                examples += 1
        
    for room in rooms:
        if intent_type == 'aumentarBrillo':
            print 'No veo en el [{}](house_room)'.format(room)
            print 'No veo en la [{}](house_room)'.format(room)
            print 'Sigo sin ver en el [{}](house_room)'.format(room)
            print 'Sigo sin ver en la [{}](house_room)'.format(room)
            print 'Continúo sin ver en el [{}](house_room)'.format(room)
            print 'Continúo sin ver en la [{}](house_room)'.format(room)
            examples += 6
        else:
            for w in WISH:
                print '{} más oscuridad en el [{}](house_room)'.format(w, room)
                print '{} luz más tenue en el [{}](house_room)'.format(w, room)
                examples += 2
                
        for l in light:
            if intent_type == 'aumentarBrillo':
                print 'No hay suficiente luz en el [{}](house_room)'.format(room)
                print 'No hay suficiente luz en la [{}](house_room)'.format(room)
                print 'Más luz en el [{}](house_room)'.format(room)
                print 'Más luz en la [{}](house_room)'.format(room)
                print 'Demasiada oscuridad en el [{}](house_room)'.format(room)
                print 'Demasiada oscuridad en la [{}](house_room)'.format(room)
                examples += 6
                for w in WISH:
                    print '{} más {} en el [{}](house_room)'.format(w, l, room)
                    examples += 1
            else:            
                print 'Demasiada {} en el [{}](house_room)'.format(l, room)
                print 'Demasiada {} en la [{}](house_room)'.format(l, room)
                print 'Demasiado {} en el [{}](house_room)'.format(l, room)
                print 'Demasiado {} en la [{}](house_room)'.format(l, room)
                examples += 4
    
    while examples < MAX_EXAMPLES - 25:
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)
        if intent_type == 'aumentarBrillo':
            l = random.choice(light)
        else:
            l = 'oscuridad'
        print '{} el {} en un [{}](percent) en el [{}](house_room)'.format(f, l, perc, room)
        print '{} la {} en un [{}](percent) en el [{}](house_room)'.format(f, l, perc, room)
        print '{} el {} en un [{}](percent) en la [{}](house_room)'.format(f, l, perc, room)
        print '{} la {} en un [{}](percent) en la [{}](house_room)'.format(f, l, perc, room)
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)
        if intent_type == 'aumentarBrillo':
            l = random.choice(light)
        else:
            l = 'oscuridad'
        print '{} el {} en el [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
        print '{} el {} en la [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
        print '{} la {} en el [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
        print '{} la {} en la [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(up)
        w = random.choice(WISH)
        if intent_type == 'aumentarBrillo':
            l = random.choice(light)
        else:
            l = 'oscuridad'       
        print 'En el [{}](house_room) {} el {} en un [{}](percent)'.format(room, f, l, perc)
        print 'En el [{}](house_room) {} la {} en un [{}](percent)'.format(room, f, l, perc)
        print 'En la [{}](house_room) {} el {} en un [{}](percent)'.format(room, f, l, perc)
        print 'En la [{}](house_room) {} la {} en un [{}](percent)'.format(room, f, l, perc)
        
        examples += 12
        
        perc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(WISH)
        if intent_type == 'aumentarBrillo':
            l = random.choice(light)
        else:
            l = 'oscuridad'        
        print '{} [{}](percent) más de {} en el [{}](house_room)'.format(w, perc, l, room)
        print '{} [{}](percent) más de {} en la [{}](house_room)'.format(w, perc, l, room)
        erc = random.choice(percentages)
        room = random.choice(rooms)
        f = random.choice(UP)
        w = random.choice(wish)
        if intent_type == 'aumentarBrillo':
            l = random.choice(light)
        else:
            l = 'oscuridad'        
        print 'En el [{}](house_room) {} [{}](percent) más de {}'.format(room, w, perc, l)
        print 'En la [{}](house_room) {} [{}](percent) más de {}'.format(room, w, perc, l)
        examples += 4
        
        if intent_type != 'aumentarBrillo':
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            l = random.choice(light)
        
            print '{} el {} en un [{}](percent) en el [{}](house_room)'.format(f, l, perc, room)
            print '{} la {} en un [{}](percent) en el [{}](house_room)'.format(f, l, perc, room)
            print '{} el {} en un [{}](percent) en la [{}](house_room)'.format(f, l, perc, room)
            print '{} la {} en un [{}](percent) en la [{}](house_room)'.format(f, l, perc, room)
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            l = random.choice(light)
            print '{} el {} en el [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
            print '{} el {} en la [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
            print '{} la {} en el [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
            print '{} la {} en la [{}](house_room) en un [{}](percent)'.format(f, l, room, perc)
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(down)
            w = random.choice(WISH)
            l = random.choice(light)
            print 'En el [{}](house_room) {} el {} en un [{}](percent)'.format(room, f, l, perc)
            print 'En el [{}](house_room) {} la {} en un [{}](percent)'.format(room, f, l, perc)
            print 'En la [{}](house_room) {} el {} en un [{}](percent)'.format(room, f, l, perc)
            print 'En la [{}](house_room) {} la {} en un [{}](percent)'.format(room, f, l, perc)
            
            examples += 12
            
            perc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(WISH)
            l = random.choice(light)
            print '{} [{}](percent) menos de {} en el [{}](house_room)'.format(w, perc, l, room)
            print '{} [{}](percent) menos de {} en la [{}](house_room)'.format(w, perc, l, room)
            erc = random.choice(percentages)
            room = random.choice(rooms)
            f = random.choice(DOWN)
            w = random.choice(wish)
            l = random.choice(light)
            print 'En el [{}](house_room) {} [{}](percent) menos de {}'.format(room, w, perc, l)
            print 'En la [{}](house_room) {} [{}](percent) menos de {}'.format(room, w, perc, l)
            examples += 4
