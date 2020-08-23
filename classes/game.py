#!usr/local/bin/python3.8
# -*- coding: utf-8 -*import
import random
from typing import List, Dict
from classes.magic import Magic


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    ACTIONS = ['Attack', 'Magic', 'Items']

    def __init__(self, name, hp: int, mp: int, attack: int, defence: int,
                 magic: List[Magic], items: List[Dict]):
        self.name = name
        self.__max_hp = hp
        self.hp = hp
        self.__max_mp = mp
        self.mp = mp
        self.__attack = attack
        self.defence = defence
        self.magic = magic
        self.items = items

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def max_mp(self):
        return self.__max_mp

    def damage(self):
        attack_low = self.__attack - 20
        attack_high = self.__attack + 20
        return random.randrange(attack_low, attack_high)

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def reduce_mp(self, cost: int):
        self.mp -= cost

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.__max_hp:
            self.hp = self.__max_hp

    def choose_action(self):
        i = 1
        print(f'\n{BColors.OKBLUE}{BColors.BOLD}{self.name} Turn:\n{BColors.ENDC}')
        print(f'{BColors.OKBLUE}{BColors.BOLD}ACTIONS{BColors.ENDC}')
        for action in Person.ACTIONS:
            print(f"    {i}. {action}")
            i += 1

    def choose_magic(self):
        i = 1
        print(f'{BColors.OKBLUE}{BColors.BOLD}MAGIC{BColors.ENDC}')
        for magic in self.magic:
            print(f"    {i}. {magic.name}, (cost: {magic.mp_cost})")
            i += 1

    def choose_item(self):
        i = 1
        print(f"{BColors.OKGREEN}{BColors.BOLD}ITEMS:{BColors.ENDC}")
        for item in self.items:
            print(f"    {i}. {item['item'].name}: {item['item'].description} (x{item['quantity']})")
            i += 1

    @staticmethod
    def choose_target(enemies):
        i = 1
        alive_enemies = len([x for x in enemies if x.hp > 0])
        print(f"\n{BColors.OKGREEN}{BColors.BOLD}TARGET:{BColors.ENDC}")
        for enemy in enemies:
            if enemy.hp != 0:
                print(f"    {i}. {enemy.name}")
                i += 1
        while True:
            choice = int(input("Choose target: ")) - 1
            if choice in range(1, alive_enemies + 1) or choice == 0:
                break
            print("Wrong magic number! Choose again!")
        return choice

    def get_stats(self):
        tick = '█'
        hp_ticks = int(((self.hp / self.__max_hp) * 100) / 4)
        hp_bar = ''

        # dynamic HP bar
        for x in range(hp_ticks):
            hp_bar += tick

        while True:
            if len(hp_bar) == 25:
                break
            hp_bar += ' '

        # Dynamic MP bar
        mp_ticks = int(((self.mp / self.__max_mp) * 100) / 10)
        mp_bar = ''

        for x in range(mp_ticks):
            mp_bar += tick

        while True:
            if len(mp_bar) == 10:
                break
            mp_bar += ' '

        # Keep HP 4 spaces
        hp = str(self.hp)
        if len(hp) < 2:
            hp = f"   {hp}"
        elif len(hp) < 3:
            hp = f"  {hp}"
        elif len(hp) < 4:
            hp = f' {hp}'

        # Keep MP 3 spaces
        mp = str(self.mp)
        if len(mp) < 2:
            mp = f'  {mp}'
        elif len(mp) < 3:
            mp = f' {mp}'

        print(f'                     {BColors.BOLD}_________________________            __________{BColors.ENDC}')
        print(f'{BColors.BOLD}{self.name}:    {hp}/{self.__max_hp} '
              f'|{BColors.OKGREEN}{hp_bar}{BColors.ENDC}'
              f'{BColors.BOLD}|   {mp}/{self.__max_mp}|{BColors.OKBLUE}{mp_bar}{BColors.ENDC}{BColors.BOLD}|'
              f'{BColors.ENDC}')

    def get_enemy_stats(self):
        hp_bar = ''
        bar_ticks = int(((self.hp / self.__max_hp) * 100) / 2)
        tick = '█'

        for x in range(bar_ticks):
            hp_bar += tick

        while True:
            if len(hp_bar) == 50:
                break
            hp_bar += ' '

        # Keep HP 4 spaces
        hp = str(self.hp)
        if len(hp) < 2:
            hp = f"    {hp}"
        elif len(hp) < 3:
            hp = f"   {hp}"
        elif len(hp) < 4:
            hp = f'  {hp}'
        elif len(hp) < 5:
            hp = f" {hp}"

        print(f'                     {BColors.BOLD}__________________________________________________{BColors.ENDC}')
        print(f'{BColors.BOLD}{self.name}  {hp}/{self.__max_hp} '
              f'|{BColors.FAIL}{hp_bar}{BColors.ENDC}'
              f'{BColors.BOLD}|{BColors.ENDC}')

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        hp_breakpoint = self.hp / self.__max_hp * 100

        if self.mp < spell.mp_cost or (spell.type == 'white' and hp_breakpoint > 50):
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
