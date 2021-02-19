class GameOver(Exception):

    def __init__(self, player):
        self.player = player
        self.scores_write()
        print(f'Your score: {player.score}.')

    def scores_write(self):
        file = open('scores.txt', 'a')
        file.writelines(f"{self.player.name}: {self.player.score} \n")
        file.close()
        self.score_sort()

    @staticmethod
    def score_sort():
        file = open('scores.txt', 'r')
        lines = file.readlines()
        file.close()

        lines = list(map(str.split, lines))
        lines.sort(key=lambda x: int(x[1]), reverse=True)

        file = open('scores.txt', 'w')
        for line in lines[:10]:
            file.writelines(f"{line[0]} {line[1]} \n")

        file.close()


class EnemyDown(Exception):
    pass


class WrongInput(ValueError):
    pass
