# -*- coding:utf-8 -*-

import random

print 'hello world'

hidden = random.randint(1, 100)

i = 0
while i < 7:
    guess = int(raw_input())

    if guess == hidden:
        print 'you nailed it', guess
        break
    elif guess > hidden:
        print 'your guess is bigger'
    else:
        print 'your guess is smaller'

    i += 1
else:
    print 'failed'
