# -*- coding: utf-8 -*-

board = [[1, 1, 2, 2, 2, 2],
         [1, 1, 1, 3, 3, 2],
         [1, 1, 3, 3, 3, 2],
         [4, 5, 5, 3, 3, 2],
         [4, 1, 1, 3, 2, 2],
         [4, 4, 1, 3, 3, 2]]

# mini_board : 2차원 리스트(리스트의 리스트)로 그림판을 나타냄
# x, y : 각각 그림판에서 선택한 픽셀의 행과 열을 나타냄
# color : 새로 칠하게 될 색 값을 나타냄
# 모든 인접한 주변의 같은 색깔을 새로운 color로 칠함
def fill(mini_board, x, y, color):
    pass

# mini_board : 2차원 리스트(리스트의 리스트)로 그림판을 나타냄
# 해당 보드를 화면에 출력
def show(mini_board):
    pass

# 최초에 그림판의 상태를 보여줌
show(board)

while True:
    print('please intert key..')
    print('f -> fill q -> quit')

    # 사용자에게 커맨드를 입력 받음
    cmd = input()

    if cmd == 'f':
        print 'insert x, y index & color'

        # 3 4 5와 같은 형식으로, 띄어쓰기를 기준으로 각각 인덱스와 색의 값을 받음
        index = raw_input()
        x, y, color = map(int, index.split(' '))

        try:
            fill(board, x, y, color)
        except:
            print('invalid index')

        show(board)

    elif cmd == 'q': # q인 경우 프로그램 종료
        break
    else:
        print('no command available')
