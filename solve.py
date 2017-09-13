def main():
    init_pos = 4
    print(init_pos)
#   print(solve(init_pos, primitive, generate_moves, do_move))

def primitive(pos):
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
