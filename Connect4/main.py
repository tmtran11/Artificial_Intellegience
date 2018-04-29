"""# Minimax algorithm
# alpha-beta prune
# best order prune
# estimate function for non_terminal node
# use machine learning to find weight for estimate function

# connect4
# board 6*7

"""
"""
from test import test_heap_max
from test import test_heap_min
from test import test_eval
from test import test_produce
from test import test_minimax
test_heap_max()
test_heap_min()
test_eval()
test_produce()
test_minimax()
"""

from game import Game
from agent import Agent
from human import Human

agent = Agent()
human1 = Human()
human2 = Human()
#game = Game(human1,human2)
game = Game(agent,human1)
game.game()
