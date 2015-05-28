""" Chris's Color data base
"""


base03 = '\033[1;30m'
base02 = '\033[0;30m'
base01 = '\033[1;32m'
base00 = '\033[1;33m'
base0  = '\033[1;34m'
base1  = '\033[1;36m'
base2  = '\033[0;37m'
base3  = '\033[1;37m'
yellow = '\033[0;33m'
orange = '\033[1;31m'
red    = '\033[0;31m'
magenta= '\033[0;35m'
violet = '\033[1;35m'
blue   = '\033[0;34m'
cyan   = '\033[0;36m'
green  = '\033[0;32m'
reset  = '\033[0m'
clear  = '\033[H\033[2J'

import random
def random_color():
    return random.choice([yellow, orange, red, magenta, violet, blue, cyan, green])

def clear_screen():
    print(clear,end='')


if __name__=='__main__':
    print(clear)
    print(base03 + 'Base03' + reset, end=' ')
    print(base02 + 'Base02' + reset, end=' ')
    print(base01 + 'Base01' + reset, end=' ')
    print(base00 + 'Base00' + reset, end=' ')
    print(base0 + 'base00' + reset, end=' ')
    print(base1 + 'base1' + reset, end=' ')
    print(base2 + 'base2' + reset, end=' ')
    print(base3 + 'base3' + reset, end=' ')
    
    print()

    print(yellow + 'yellow' + reset, end=' ')
    print(orange + 'orange' + reset, end=' ')
    print(red + 'red' + reset, end=' ')
    print(magenta + 'magenta' + reset, end=' ')
    print(violet + 'violet' + reset, end=' ')
    print(blue + 'blue' + reset, end=' ')
    print(cyan + 'cyan' + reset, end=' ')
    print(green + 'green' + reset, end=' ')
    print(reset + 'reset' + reset, end=' ')
    print(clear + 'clear' + reset, end=' ')

    print()

    for count in range(7):
        print(random_color() + 'Random' + reset, end=' ')
    print()
