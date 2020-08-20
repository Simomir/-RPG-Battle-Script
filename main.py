#!usr/local/bin/python3.8
# -*- coding: utf-8 -*import
from classes.game import Person, BColors
from classes.magic import Magic


Fire = Magic('Fire', 10, 60)
Thunder = Magic('Thunder', 12, 50)
Blizzard = Magic('Blizzard', 15, 70)
spells = [Fire, Thunder, Blizzard]


player = Person(460, 65, 60, 34, spells)
enemy = Person(1200, 65, 45, 25, spells)

running = True
print(f"{BColors.FAIL}{BColors.BOLD}AN ENEMY ATTACKS!{BColors.ENDC}")

while running:
    print('=' * 30)
    player.choose_action()
    correct = False
    while True:
        choice = int(input('Choose action: '))
        if choice in range(1, 3):
            correct = True
            break
        print("Wrong action number! Choose again!")
    idx = choice - 1

    if idx == 0:
        damage = player.damage()
        enemy.take_damage(damage)

    running = False