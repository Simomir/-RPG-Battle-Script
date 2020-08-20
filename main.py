#!usr/local/bin/python3.8
# -*- coding: utf-8 -*import
from classes.game import Person, BColors
from classes.magic import Magic

# Create Black Magic
Fire = Magic('Fire', 10, 95, 'black')
Thunder = Magic('Thunder', 12, 141, 'black')
Blizzard = Magic('Blizzard', 15, 124, 'black')
Meteor = Magic('Meteor', 30, 240, 'black')
Quake = Magic('Quake', 18, 135, 'black')

# Create White Magic
Cure = Magic("Cure", 12, 120, 'white')
Cura = Magic("Cura", 18, 200, 'white')


player_spells = [Fire, Thunder, Blizzard, Meteor, Cure, Cura]
enemy_spells = []

# Create opponents
player = Person(460, 65, 60, 34, player_spells)
enemy = Person(1200, 65, 45, 25, enemy_spells)

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
        spell = player.magic[idx]
        spell_name = spell.name
        cost = spell.mp_cost
        current_player_mp = player.mp

        if cost > current_player_mp:
            print(f"{BColors.FAIL}\nNot enough MP\n{BColors.ENDC}")
            continue

        player.reduce_mp(cost)
        magic_damage = spell.generate_damage()

        if spell.type == 'white':
            player.heal(magic_damage)
            print(f"{BColors.OKBLUE}\n{spell_name} heals for {magic_damage} HP.{BColors.ENDC}")
        elif spell.type == 'black':
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
