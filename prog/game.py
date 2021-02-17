from prog.exceptions import EnemyDown, GameOver
from prog.models import Player, Enemy


def start_game(foe, player, level):
    while True:
        try:
            player.attack(foe)
        except EnemyDown:
            player.score += 5
            level += 1
            foe = Enemy(level=level)
            print('You Win! Level up.')
        player.defence(foe)


def help_me():
    file = open('requirements.txt', 'r')
    for line in file:
        print(line[:-1])
    file.close()


def exit_game(player):
    raise GameOver(player)


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
    comands = {'start': lambda: start_game(foe, player, level),
               'help': lambda: help_me(),
               'exit': lambda: exit_game(player),
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



