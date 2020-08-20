#!usr/local/bin/python3.8
# -*- coding: utf-8 -*import
from classes.game import Person, BColors
from classes.magic import Magic


Fire = Magic('Fire', 10, 95)
Thunder = Magic('Thunder', 12, 141)
Blizzard = Magic('Blizzard', 15, 124)
spells = [Fire, Thunder, Blizzard]


player = Person(460, 65, 60, 34, spells)
enemy = Person(1200, 65, 45, 25, spells)

running = True
print(f"{BColors.FAIL}{BColors.BOLD}AN ENEMY ATTACKS!{BColors.ENDC}")

while running:
    print('=' * 30)

    # Player attack move
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
        print(f"You attacked for {damage} points of damage. Enemy HP: {enemy.hp}")

    elif idx == 1:
        player.choose_magic()
        correct = False
        while True:
            choice = int(input("Choose magic: "))
            if choice in range(1, len(player.magic) + 1):
                correct = True
                break
            print("Wrong magic number! Choose again!")
        idx = choice - 1
        spell = player.get_magic_name(idx)
        cost = player.get_magic_mp_cost(idx)
        current_player_mp = player.mp

        if cost > current_player_mp:
            print(f"{BColors.FAIL}\nNot enough MP\n{BColors.ENDC}")
            continue

        player.reduce_mp(cost)
        magic_damage = player.magic_damage(idx)
        enemy.take_damage(magic_damage)
        print(f"{BColors.OKBLUE}\n{spell} deals {magic_damage} points of damage.{BColors.ENDC}")

    # Enemy attack move
    enemy_choice = 1
    enemy_damage = enemy.damage()
    player.take_damage(enemy_damage)
    print(f"Enemy attacks for {enemy_damage} points of damage.")
    print('-' * 30)
    print(f"Enemy HP: {BColors.FAIL}{enemy.hp} / {enemy.max_hp()}{BColors.ENDC}\n"
          f"Your HP: {BColors.OKGREEN}{player.hp} / {player.max_hp()}{BColors.ENDC}\n"
          f"Your MP: {BColors.OKBLUE}{player.mp} / {player.max_mp()}{BColors.ENDC}\n")

    # check if someone is dead
    if enemy.hp == 0:
        print(f"{BColors.OKGREEN}You win!{BColors.ENDC}")
        running = False
    elif player.hp == 0:
        print(f"{BColors.FAIL}Your enemy has defeated you!{BColors.ENDC}")
        running = False
