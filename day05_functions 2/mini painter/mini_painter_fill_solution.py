# -*- coding: utf-8 -*-

board = [[1, 1, 2, 2, 2, 2],
         [1, 1, 1, 3, 3, 2],
         [1, 1, 3, 3, 3, 2],
         [4, 5, 5, 3, 3, 2],
         [4, 1, 1, 3, 2, 2],
         [4, 4, 1, 3, 3, 2]]

def fill_bfs(mini_board, x, y, color):
     if not (0 <= x < len(mini_board) \
         and 0 <= y < len(mini_board[0])):
         raise Exception('invalid index')

     org_color = mini_board[x][y]
     queue = [(x, y)]

     while queue:
         cx, cy = queue.pop(0)
         mini_board[cx][cy] = color

         for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
             new_x = cx + dx
             new_y = cy + dy

             if 0 <= new_x < len(mini_board) and 0 <= new_y < len(mini_board[0]) \
                and org_color == mini_board[new_x][new_y]:
                queue.append((new_x, new_y))


def fill_dfs(mini_board, x, y, color):
    if not (0 <= x < len(mini_board) \
        and 0 <= y < len(mini_board[0])):
        raise Exception('invalid index')

    org_color = mini_board[x][y]
    mini_board[x][y] = color

    for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < len(mini_board) and 0 <= new_y < len(mini_board[0]) \
            and org_color == mini_board[new_x][new_y]:
            fill(mini_board, new_x, new_y, color)

def show(mini_board):
    for row in mini_board:
        for item in row:
            print(item, sep=' ', end='')
        print()

show(board)

while True:
    print('please intert key..')
    print('f -> fill q -> quit')

    cmd = input()
    if cmd == 'f':
        print('insert x, y index & color')
        index = input()
        x, y, color = map(int, index.split(' '))

        try:
            fill_bfs(board, x, y, color)
        except:
            print('invalid index')

        show(board)

    elif cmd == 'q':
        break
    else:
        print('no command available')
