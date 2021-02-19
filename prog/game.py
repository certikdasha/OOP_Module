from prog.exceptions import EnemyDown, GameOver, WrongInput
from prog.models import Player, Enemy


def start_game(foe, player, level, is_attack):
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
            pass


def help_me():
    file = open('settings.txt.txt', 'r')
    commands = file.readlines()
    for line in commands[1:]:
        print(line[:-1])
    file.close()


def show_scores():
    file = open('scores.txt', 'r')
    for line in file:
        print(line[:-1])
    file.close()


def play():
    user_name = input('Enter your name: ')
    player = Player(name=user_name)
    level = 1
    foe = Enemy(level=level)
    # mess = input(f'Hi, {player.name}, what do you want? \n')
    comands = {'start': lambda: start_game(foe, player, level, True),
               'help': lambda: help_me(),
               'exit': lambda: player.exit_game(),
               'show scores': lambda: show_scores(),
            }
    while True:
        a = input()
        comands[a]()


if __name__ == '__main__':
    try:
        play()
    except GameOver as e:
        print(f'Game Over!')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')



