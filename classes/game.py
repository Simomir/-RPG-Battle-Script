#!usr/local/bin/python3.8
# -*- coding: utf-8 -*import
import random
from classes.inventory import Item
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

    def __init__(self, hp: int, mp: int, attack: int, defence: int,
                 magic: List[Magic], items: List[Dict]):
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

    @staticmethod
    def choose_action():
        i = 1
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
