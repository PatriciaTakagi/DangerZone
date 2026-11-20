#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1Bg{i}',(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Playerplane':
                return Player('Playerplane',(10,WIN_HEIGHT/2))
            case 'Enemyplane1':
                return Enemy('Enemyplane1',(WIN_WIDTH +10,random.randint(40, WIN_HEIGHT -100)))
            case 'Enemyplane2':
                return Enemy('Enemyplane2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -100)))





