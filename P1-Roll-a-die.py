from random import *

inp = input('Roll a die? y/n: ').lower()
if(inp not in ['y','n']):
        print('Invalid Input!')
        inp = input('Roll a die? y/n: ').lower()

while(inp == 'y'):
    num = randint(1,6)

    if (num == 1):
        print("[       ]\n[  ♣️    ]\n[       ]#1") 
    if (num == 2):
        print("[  ♣️    ]\n[       ]\n[  ♣️    ]#2")
    if (num == 3):
        print("[  ♣️    ]\n[  ♣️    ]\n[  ♣️    ]#3")
    if (num == 4):
        print("[♣️   ♣️  ]\n[       ]\n[♣️   ♣️  ]#4")
    if (num == 5):
        print("[♣️   ♣️  ]\n[  ♣️    ]\n[♣️   ♣️  ]#5")
    if (num == 6):
        print("[♣️   ♣️  ]\n[♣️   ♣️  ]\n[♣️   ♣️  ]#6")
    
    inp = input('Roll a die? y/n: ').lower()

    if(inp not in ['y','n']):
        print('Invalid Input!')
        inp = input('Roll a die? y/n: ').lower()
    
print('Thanks for playing!♣️')

    
        