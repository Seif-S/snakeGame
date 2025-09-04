import os
import time
import keyboard
import random

def main():
    snake = 'o'
    snakePos = []
    snakeLenght = 3
    food = 'O'
    wall = '#'
    borderWidth = 10
    borderHeight = 10
    clear = lambda: os.system('cls')

    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('left', left)
    keyboard.add_hotkey('down', down)
    keyboard.add_hotkey('right', right)

    stageMap = initDrawMap(wall, borderWidth, borderHeight)

    for i in range(snakeLenght):
        snakePos.append((2, 2 + i))
        stageMap[2][2 + i] = snake

    stageMap = spawnFood(stageMap, food, borderWidth, borderHeight)

    global lastKey 
    lastKey = 'right'

    while True:
        clear()
        for i in stageMap:
            print(' '.join(map(str, i)))

        Heady, Headx = snakePos[-1]
        Taily, Tailx = snakePos[0]

        if lastKey == 'right':
            if stageMap[Heady][Headx + 1] is not wall and stageMap[Heady][Headx + 1] is not snake:
                stageMap[Heady][Headx + 1] = snake
                stageMap[Taily][Tailx] = ' '
                snakePos.append((Heady, Headx + 1))
                snakePos.pop(0)
            else:
                break
        
        if lastKey == 'up':
            if stageMap[Heady - 1][Headx] is not wall and stageMap[Heady - 1][Headx] is not snake:
                stageMap[Heady - 1][Headx] = snake
                stageMap[Taily][Tailx] = ' '
                snakePos.append((Heady - 1, Headx))
                snakePos.pop(0)
            else:
                break

        if lastKey == 'left':
            if stageMap[Heady][Headx - 1] is not wall and stageMap[Heady][Headx - 1] is not snake:
                stageMap[Heady][Headx - 1] = snake
                stageMap[Taily][Tailx] = ' '
                snakePos.append((Heady, Headx - 1))
                snakePos.pop(0)
            else:
                break

        if lastKey == 'down':
            if stageMap[Heady + 1][Headx] is not wall and stageMap[Heady + 1][Headx] is not snake:
                stageMap[Heady + 1][Headx] = snake
                stageMap[Taily][Tailx] = ' '
                snakePos.append((Heady + 1, Headx))
                snakePos.pop(0)
            else:
                break
        time.sleep(1)
    print('Game over')

def spawnFood(stage, food, width, height):
    foodPosX = random.randrange(1, width)
    foodPosY = random.randrange(1, height)
    while True:
        if stage[foodPosY][foodPosX] is not ' ':
            continue
        else:
            stage[foodPosY][foodPosX] = food
            break
    return stage

def initDrawMap(object: str, width: int, height: int) -> list:
    # create the basic layout of the map
    stageMap = []
    for i in range(height):
        stageMap.append([])
        for index in range(width):
            if i == 0 or i + 1 == height or index == 0 or index + 1 == width:
                stageMap[i].append(object)
                continue
            else:
                stageMap[i].append(' ')
                continue
    return stageMap

def drawMap():
    pass

def up():
    global lastKey 
    lastKey = 'up'

def left():
    global lastKey
    lastKey = 'left'

def down():
    global lastKey
    lastKey = 'down'

def right():
    global lastKey
    lastKey = 'right'


if __name__ == '__main__':
    main()