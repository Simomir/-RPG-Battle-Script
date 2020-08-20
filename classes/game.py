#!usr/local/bin/python3.8
# -*- coding: utf-8 -*import
import random
from typing import List
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
    ACTIONS = ['Attack', 'Magic']

    def __init__(self, hp: int, mp: int, attack: int, defence: int, magic: List[Magic]):
        self.__max_hp = hp
        self.hp = hp
        self.__max_mp = mp
        self.mp = mp
        self.__attack = attack
        self.defence = defence
        self.magic = magic

    def max_hp(self):
        return self.__max_hp

    def max_mp(self):
        return self.__max_mp

    def damage(self):
        attack_low = self.__attack - 20
        attack_high = self.__attack + 20
        return random.randrange(attack_low, attack_high)

    def magic_damage(self, idx):
        magic_damage = self.magic[idx].damage
        damage_low = magic_damage - 10
        damage_high = magic_damage + 10
        return random.randrange(damage_low, damage_high)

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def reduce_mp(self, cost: int):
        self.mp -= cost

    @staticmethod
    def choose_action():
        i = 1
        print('Actions')
        for action in Person.ACTIONS:
            print(f"{i}: {action}")
            i += 1

    def choose_magic(self):
        i = 1
        print('Magic')
        for magic in self.magic:
            print(f"{i}: {magic.name}, (cost: {magic.mp_cost})")
            i += 1
