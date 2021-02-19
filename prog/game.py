'''
запуск игры
'''
from prog.exceptions import EnemyDown, GameOver, WrongInput
from prog.models import Player, Enemy


def start_game(foe, player, level, is_attack):
    '''
    :param foe: обьект противника
    :param player: обьект игрока
    :param level: уровень
    :param is_attack: определение атака/защита
    '''
    while True:
        try:
            if is_attack:
                player.attack(foe)
                is_attack = False
            else:
                pass
        except EnemyDown:
            player.score += 5
            level += 1
            foe = Enemy(level=level)
            print('You Win! Level up.')
        except WrongInput:
            print('incorrect value')
            continue
        try:
            player.defence(foe)
            is_attack = True
        except WrongInput:
            print('incorrect value')


def help_me():
    '''
    output to the user possible commands
    '''
    file = open('settings.txt', 'r')
    commands = file.readlines()
    for line in commands[1:]:
        print(line[:-1])
    file.close()


def show_scores():
    '''
    output to the user of the top-10 players
    '''
    file = open('scores.txt', 'r')
    for line in file:
        print(line[:-1])
    file.close()


def play():
    '''
    game functionality
    '''
    user_name = input('Enter your name: ')
    player = Player(name=user_name)
    level = 1
    foe = Enemy(level=level)
    comands = {'start': lambda: start_game(foe, player, level, True),
               'help': help_me,
               'exit': player.exit_game,
               'show scores': show_scores,
            }
    while True:
        enter = input()
        comands[enter]()


if __name__ == '__main__':
    try:
        play()
    except GameOver as element:
        print('Game Over!')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')
