def main():
    print(init_pos)
    print(solve(init_pos, primitive, generate_moves, do_move))

def solve(init_pos, primitive, generate_moves, do_move):
    results = []
    moves = generate_moves(init_pos)
    for move in moves:
        result = primitive(do_move(init_pos, move))
        if result == 'L':
            results += [opposite(result)]
        else:
            results += [opposite(solve(init_pos-move, primitive, generate_moves, do_move))]
        #recursive step
    if 'W' in results:
        return 'W'
    else:
        return 'L'

            
def opposite(DWULT):
    if DWULT == 'L':
        return 'W'
    else:
        return 'L'
            
# The initial position
init_pos = 4

def primitive(pos):
    """
    Return 'L' loss if players turn to take, and unable to take, aka
    pos == 0, else 'U' undecided
    >>> primitive(4)
    'U'
    >>> primitive(0)
    'L'
    """
    if pos == 0:
        return 'L'
    return 'U'

def do_move(pos, action):
    return pos - action

def generate_moves(pos):
    moves = []
    if pos >= 1:
        moves += [1]
    if pos >= 2:
        moves += [2]
    if pos >= 3:
        moves += [3]
    return moves

if __name__ == "__main__":
    main()
