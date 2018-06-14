# Artificial Intellegience algorithms.
# Self-study
# Resources from:
#   ColumbiaX - CSMM.101x, https://courses.edx.org/courses/course-v1:ColumbiaX+CSMM.101x+1T2018/course/ ,and 
#   "Artificial Intellegience: A Mordern Approach", 3rd edition, written by Staurt J.Russell and Peter Norvig

# Feature project: Connect4 - An optimized adversarial search
https://github.com/tmtran11/Artificial_Intellegience/tree/master/Connect4

*The agent’s algorithm is a version of Adversarial search. This adversarial search is a recursive depth-first search utilizing minimax decision process, in which the agent assumes that their opponent will play perfectly, and therefore, attempt to maximize its chance of winning by choosing from a successor states produce by  the oopent, who had minimizing the agent’s chance of winning.

*The agent is is implemented with specialized data structure to store object-level state; and to improve search speed of adversarial search.

*The main node:
- In each game, there is a main node represent the current state. When a move is made, the node update itself

*The minimax tree:
- Minimax tree is composed of alternatively maximizing layer and minimizing layer. Maximize layer is where agent choose the state with best value among the successive state, whose value is the minimum value of the successive state’s successor. Vice versa with minimizing layer
The value of a state is not evaluated until the deepest depth is reach! 
- Minimax tree implement alpha-beta pruning, which prune subtree that do not surpass their co-subtree in respective value. Alpha-beta pruning is speeded up by using node-ordering, which return node is sorted-order and hence speed up the comparison. Node is sorted using heap, either heap_min or heap_max, depend on either the maximize or minimize algorithm is running.

*Heap:
- Heap structure, where root element is always bigger/smaller than all other element in tree. Heap is always sorted with add and remove functionality run in O(log n).

*The agent use a heuristic to evaluate, in which the heuristic will scan all possible 4-sequence in row, column and diagonal. The returned value is the the sum of all sum of the each sequence power of by 2, where there are point deduced if the sequence is an interruptive sequence (all cell is fill with either attacker’s or defender’s, and therefore, no chance to develop), and there are points added (significantly bigger) to winning sequence.

*The game can be played between human and human, agent, and agent, agent and human. The behavior of the agent is change interesting according to the depth of there adversarial search tree. Minimax tree is optimal enough that the agent is able to run sufficiently fast if given any depth from 1 to 5.

