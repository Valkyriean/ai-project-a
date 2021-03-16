"""
COMP30024 Artificial Intelligence, Semester 1, 2021
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json
import search.ai_util as au

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import print_board, print_slide, print_swing


# key: cur 当前坐标tuple
# value: [[]upper/lower, r/s/p/b],[...]]
# board_dict = {}

# 记录每个棋子的每一步的走法
# ("r", [(0,0),(1,0)])
# friendly_list = []

def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)



    friendly_list, enemy_list, block_list = au.eat_enemy(data)
    max_round = au.makeup_rest(friendly_list, enemy_list, block_list)
    au.print_path(max_round, friendly_list, enemy_list, block_list)

