from Clock import Clock
import time
import pygame

RIGHT = 0
BOT = 157
LEFT = 314
TOP = 472
blackColor = (0, 0, 0)
colSize = 15
framerate = 90
patternTime = 13*framerate
clockTime = 8*framerate
counter = 0


def setup():
    global clock, rowSize, screen
    pygame.init()
    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Wall Clock')
    clock = []
    radius = width/(colSize*2)
    rowSize = int(height/(radius*2))
    for i in range(rowSize):
        rowClock = []
        for j in range(colSize):
            rowClock.append(
                Clock((j*2+1) * radius, (i*2+1) * radius, radius, 1))
        clock.append(rowClock)


def main():
    global counter
    timer = pygame.time.Clock()
    currentMinute = time.localtime().tm_min
    setup()
    setPattern(4)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if currentMinute != time.localtime().tm_min:
            currentMinute = time.localtime().tm_min
            setPattern(4)
            counter = 0

        for i in range(4):
            if counter == clockTime + patternTime*i:
                setPattern(i)
                break

        draw()
        counter += 1
        if counter == clockTime + patternTime*4:
            counter = clockTime
        timer.tick(framerate)
        pygame.display.update()


def draw():
    screen.fill(blackColor)
    if Clock.patternSetting:
        Clock.patternSetting = False
        for i in clock:
            for j in i:
                j.settingPattern()
            if any(obj.patternSetting for obj in i):
                Clock.patternSetting = True
    else:
        for i in clock:
            for j in i:
                j.update()
    for i in clock:
        for j in i:
            j.display(screen)


def setPattern(pattern):
    Clock.patternSetting = True
    if pattern == 0:
        distance = 10
        for i in range(len(clock)):
            for j in range(len(clock[i])):
                clock[i][j].reinitiate(
                    j*distance + BOT, j*distance + TOP, 0, 0, True)

    if pattern == 1:
        for i in range(len(clock)):
            baseAngle = (i % 2) * LEFT
            for j in range(len(clock[i])):
                k = (j+i) % 2
                clock[i][j].reinitiate(
                    k*BOT + baseAngle, (k+1)*BOT + baseAngle, 1, 0, True)

    elif pattern == 2:
        for i in range(len(clock)):
            baseAngle = (i % 2) * LEFT
            for j in range(len(clock[i])):
                k = (j+i) % 2
                clock[i][j].reinitiate(
                    k*BOT + baseAngle, (k+1)*BOT + baseAngle, (i+j) % 2, (i+j) % 2, True)

    elif pattern == 3:
        distance = 10
        for i in range(len(clock)):
            for j in range(len(clock[i])):
                clock[i][j].reinitiate(0, LEFT, 1, 1, True)
    elif pattern == 4:
        for i in range(len(clock)):
            for j in range(len(clock[i])):
                clock[i][j].reinitiate(135, 135, 1, 0, False)

        topDistance = -((rowSize-6) // -2)
        leftDistance = -((colSize-13) // -2)
        digitMaker[time.localtime().tm_hour // 10](topDistance, leftDistance)
        digitMaker[time.localtime().tm_hour % 10](topDistance, leftDistance+3)
        digitMaker[time.localtime().tm_min // 10](topDistance, leftDistance+7)
        digitMaker[time.localtime().tm_min % 10](topDistance, leftDistance+10)


def createZero(row, col):
    for i in range(row, row+5):
        for j in range(col, col+3):
            clock[i][j].reinitiate(TOP, BOT, 1, 0,  False)
    clock[row][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+5][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+5][col+2].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+1][col+1].reinitiate(BOT, BOT, 1, 0,  False)
    clock[row+4][col+1].reinitiate(TOP, TOP, 1, 0,  False)
    clock[row][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row+5][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)


def createOne(row, col):
    clock[row][col+1].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+1][col+1].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col+1].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col+1].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+4][col+1].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col+1].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+1][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+4][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col+2].reinitiate(LEFT, TOP, 1, 0,  False)


def createTwo(row, col):
    clock[row][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+1][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+2][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+3][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+4][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row+1][col+1].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+2][col+1].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+3][col+1].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+4][col+1].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+5][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+1][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col+2].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+4][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+5][col+2].reinitiate(LEFT, TOP, 1, 0,  False)


def createThree(row, col):
    clock[row][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+1][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+2][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+3][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+4][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+5][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row+1][col+1].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+2][col+1].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+3][col+1].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+4][col+1].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+5][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+1][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+4][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col+2].reinitiate(LEFT, TOP, 1, 0,  False)


def createFour(row, col):
    clock[row][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+1][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+1].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+1][col+1].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col+1].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+3][col+1].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+4][col+1].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col+1].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+1][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+4][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col+2].reinitiate(LEFT, TOP, 1, 0,  False)


def createFive(row, col):
    clock[row][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+1][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+4][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+5][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row+1][col+1].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+2][col+1].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+3][col+1].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+4][col+1].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+5][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+1][col+2].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+2][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+3][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+4][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col+2].reinitiate(LEFT, TOP, 1, 0,  False)


def createSix(row, col):
    clock[row][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+1][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+4][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row+1][col+1].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+2][col+1].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+3][col+1].reinitiate(BOT, BOT, 1, 0,  False)
    clock[row+4][col+1].reinitiate(TOP, TOP, 1, 0,  False)
    clock[row+5][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+1][col+2].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+2][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+3][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+4][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col+2].reinitiate(LEFT, TOP, 1, 0,  False)


def createSeven(row, col):
    clock[row][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+1][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+3][col].reinitiate(BOT, 549, 1, 0,  False)
    clock[row+4][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row+1][col+1].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+2][col+1].reinitiate(235, TOP, 1, 0,  False)
    clock[row+3][col+1].reinitiate(BOT, 549, 1, 0,  False)
    clock[row+4][col+1].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col+1].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+1][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col+2].reinitiate(235, TOP, 1, 0,  False)


def createEight(row, col):
    for i in range(row, row+5):
        for j in range(col, col+3):
            clock[i][j].reinitiate(TOP, BOT, 1, 0,  False)
    clock[row][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+5][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+5][col+2].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+1][col+1].reinitiate(174, 139, 1, 0,  False)
    clock[row+2][col+1].reinitiate(453, 488, 1, 0,  False)
    clock[row+3][col+1].reinitiate(174, 139, 1, 0,  False)
    clock[row+4][col+1].reinitiate(453, 488, 1, 0,  False)
    clock[row][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row+5][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)


def createNine(row, col):
    clock[row][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+1][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row+4][col].reinitiate(RIGHT, BOT, 1, 0,  False)
    clock[row+5][col].reinitiate(TOP, RIGHT, 1, 0,  False)
    clock[row][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row+1][col+1].reinitiate(BOT, BOT, 1, 0,  False)
    clock[row+2][col+1].reinitiate(TOP, TOP, 1, 0,  False)
    clock[row+3][col+1].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+4][col+1].reinitiate(LEFT, TOP, 1, 0,  False)
    clock[row+5][col+1].reinitiate(RIGHT, LEFT, 1, 0,  False)
    clock[row][col+2].reinitiate(BOT, LEFT, 1, 0,  False)
    clock[row+1][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+2][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+3][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+4][col+2].reinitiate(BOT, TOP, 1, 0,  False)
    clock[row+5][col+2].reinitiate(LEFT, TOP, 1, 0,  False)


digitMaker = [createZero, createOne, createTwo, createThree, createFour,
              createFive, createSix, createSeven, createEight, createNine]

if __name__ == '__main__':
    main()
