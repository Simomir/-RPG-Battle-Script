#!usr/local/bin/python3.8
# -*- coding: utf-8 -*import
import random


class Magic:
    def __init__(self, name: str, mp_cost: int, damage: int, type):
        self.name = name
        self.mp_cost = mp_cost
        self.damage = damage
        self.type = type

    def generate_damage(self):
        low = self.damage - 20
        high = self.damage + 20
        return random.randrange(low, high)