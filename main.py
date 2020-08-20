#!usr/local/bin/python3.8
# -*- coding: utf-8 -*import

from classes.game import Person, BColors
from classes.magic import Magic
from classes.inventory import Item
from sys import maxsize

# Create Black Magic
Fire = Magic('Fire', 10, 95, 'black')
Thunder = Magic('Thunder', 12, 141, 'black')
Blizzard = Magic('Blizzard', 15, 124, 'black')
Meteor = Magic('Meteor', 30, 240, 'black')
Quake = Magic('Quake', 18, 135, 'black')

# Create White Magic
Cure = Magic("Cure", 12, 120, 'white')
Cura = Magic("Cura", 18, 200, 'white')

# -------------------------------------

# Create items
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
hi_potion = Item('Hi-Potion', 'potion', 'Heals 100 HP', 100)
super_potion = Item('Super Potion', 'potion', 'Heals 500 HP', 500)
elixir = Item('Elixir', 'elixir', 'Fully restores HP/MP of one party member', maxsize)
mega_elixir = Item('Mega Elixir', 'elixir', "Fully restores party's HP/MP", maxsize)
grenade = Item('Grenade', 'attack', "Deals 500 damage", 500)


player_spells = [Fire, Thunder, Blizzard, Meteor, Cure, Cura]
player_items = [potion, hi_potion, super_potion, elixir, mega_elixir, grenade]

enemy_spells = []
enemy_items = []

# Create opponents
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, enemy_spells, enemy_items)

running = True
print(f"{BColors.FAIL}{BColors.BOLD}AN ENEMY ATTACKS!{BColors.ENDC}")

while running:
    print('=' * 30)

    # Player attack move
    player.choose_action()
    correct = False
    while True:
        choice = int(input('Choose action: '))
        print()
        if choice in range(1, len(player.ACTIONS) + 1):
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
            if choice in range(1, len(player.magic) + 1) or choice == 0:
                correct = True
                break
            print("Wrong magic number! Choose again!")
        magic_idx = choice - 1

        if magic_idx == -1:
            continue

        spell = player.magic[magic_idx]
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
            print(f"{BColors.OKBLUE}{BColors.BOLD}\n{spell.name} deals {magic_damage} points of damage.{BColors.ENDC}")

    elif idx == 2:
        player.choose_item()
        correct = False
        while True:
            choice = int(input("Choose item: "))
            if choice in range(1, len(player.items) + 1) or choice == 0:
                correct = True
                break
            print("Wrong item number! Choose again!")
        item_idx = choice - 1

        if item_idx == -1:
            continue

        item = player.items[item_idx]

        if item.type == 'potion':
            amount = item.prop
            player.heal(amount)
            print(f"{BColors.OKGREEN}\n{item.name} heals for {amount} HP{BColors.ENDC}")

    # Enemy attack move
    enemy_choice = 1
    enemy_damage = enemy.damage()
    player.take_damage(enemy_damage)
    print(f"{BColors.FAIL}{BColors.BOLD}Enemy attacks for {enemy_damage} points of damage.{BColors.ENDC}")
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
