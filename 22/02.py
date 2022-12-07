with open('input_02.txt') as f:
    lines = [l.strip().split() for l in f.readlines()]

# Part 1
score = 0
for enemy_play, my_play in lines:
    enemy_num = 1 + ord(enemy_play) - ord('A')
    my_num = 1 + ord(my_play) - ord('X')
    score += my_num

    if my_num - enemy_num == 1 or my_num - enemy_num == -2:
        score += 6
    elif my_num - enemy_num == 0:
        score += 3
print(score)

# Part 2
score = 0
for enemy_play, result in lines:
    enemy_num = 1 + ord(enemy_play) - ord('A')
    if result == 'X': # Lose
        my_num = 3 if enemy_num == 1 else enemy_num - 1
    elif result == 'Y': # Draw
        my_num = enemy_num
        score += 3
    elif result == 'Z': # WIN
        my_num = 1 if enemy_num == 3 else enemy_num + 1
        score += 6
    score += my_num
print(score)
