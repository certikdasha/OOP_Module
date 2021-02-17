from random import randint
from enum import IntEnum
from .exceptions import EnemyDown, GameOver


class Enemy(object):
    def __init__(self, level):
        self.level = level
        self.lives = level


    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()
        return self.lives


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        # self.allowed_attacks = Attack()
        self.allowed_attacks = [1, 2, 3]
        self.lives = self.live()

    @staticmethod
    def live():
        setting = open('requirements.txt', 'r')
        num = setting.readline().split()
        setting.close()
        return int(num[-1])

    # возвращает результат раунда -
    # 0 если ничья, -1 если атака неуспешна, 1 если атака успешна.
    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        elif defense - attack == 1 or defense - attack == -2:
            return 1
        else:
            return -1

    # def validation(self, arg):
    #     if arg == 'exit':
    #         self.exit_game()
    #     elif int(arg) not in self.allowed_attacks:
    #         print('incorrect value')
    #         return 0

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self)
        return self.lives

    def attack(self, enemy_obj):
        attack = input('Select your attack: 1 - Wizard, 2 - Warrior, 3 - Rogue: ')
        if attack == 'exit':
            self.exit_game()
        else:
            lap = self.fight(int(attack), enemy_obj.select_attack())
            if lap == 0:
                print('It\'s a draw!')
            elif lap == 1:
                print('You attacked successfully!')
                self.score += 1
                enemy_obj.decrease_lives()
            else:
                print('You missed!')

    def defence(self, enemy_obj):
        defense = input('Select your defence: 1 - Wizard, 2 - Warrior, 3 - Rogue: ')
        if defense == 'exit':
            self.exit_game()
        else:
            lap = self.fight(enemy_obj.select_attack(), int(defense))
            if lap == 0:
                print('It\'s a draw!')
            elif lap == -1:
                print('Enemy missed!')
            else:
                print('Your defence failed')
                self.decrease_lives()

    def exit_game(self):
        raise GameOver(self)


class Attack(IntEnum):
    wizard = 1
    warrior = 2
    rogue = 3
