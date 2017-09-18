# -*- coding: utf-8 -*-

import random
import numpy as np

def show_puzzle(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            print('{:3}'.format(puzzle[i][j]), sep=' ', end='')
        print()

def initiate_puzzle(size):
    puzzle = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(i*size + j+1)
        puzzle.append(row)

    puzzle[-1][-1] = ''
    return puzzle

# list comprehension
def initiate_puzzle2(size):
    sl = range(size)
    puzzle = [[i * size + j + 1 for i in sl] for j in sl]
    puzzle[-1][-1] = ''
    return puzzle

# numpy
def initiate_puzzle3(size):
    puzzle = np.arange(1, size**2+1).reshape(size, size).tolist()
    puzzle[-1][-1] = ''
    return puzzle

def shuffle_puzzle(puzzle):
    dxs = [1, 0, -1,  0]
    dys = [0, 1,  0, -1]

    cnt = 0
    while cnt <= 300:
        rnd = random.randint(0, 3)
        dx = dxs[rnd]
        dy = dys[rnd]

        i, j = get_index(puzzle, '')
        ni = i + dx
        nj = j + dy

        if 0 <= ni < len(puzzle) and 0 <= nj < len(puzzle[0]):
            puzzle[ni][nj], puzzle[i][j] = puzzle[i][j], puzzle[ni][nj]
        cnt += 1

def is_done(puzzle, complete):
    return puzzle == complete

def get_index(puzzle, n):
    for i in range(len(puzzle)):
        try:
            index = puzzle[i].index(n)
            return i, index
        except:
            continue
    return -1, -1

def move_by_number(puzzle, n):
    i, j = get_index(puzzle, n)
    move_by_index(puzzle, i, j)

def move_by_index(puzzle, i, j):
    # movable condition
    # 좌우위아래 한방향중 하나가 '' 값이라면 이동 가능
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        new_i = i + dx
        new_j = j + dy

        if not (0 <= new_i < len(puzzle) and 0 <= new_j < len(puzzle[0])):
            continue

        if puzzle[new_i][new_j] == '':
            puzzle[i][j], puzzle[new_i][new_j] = puzzle[new_i][new_j], puzzle[i][j]
            break
    else:
        print('sorry, you cannot move that number')

# 퍼즐 생성
size = int(input(' -> please insert puzzle size : '))
puzzle = initiate_puzzle3(size)
complete = [row[:] for row in puzzle]

# 퍼즐 섞기
shuffle_puzzle(puzzle)

# 섞인 퍼즐 보기
show_puzzle(puzzle)

# 퍼즐 풀기
while not is_done(puzzle, complete):
    try:
        num = int(input(' -> select a number to move : '))
    except:
        print('give me a valid number!')
        continue
    # 움직일 수 선택하기
    move_by_number(puzzle, num)


    # 화면 clear
    import os
    cls = lambda: os.system('clear') # windows cls
    cls()

    # 움직인 이후 퍼즐 상태 보기
    show_puzzle(puzzle)

print('\nyou solved the puzzle!')
