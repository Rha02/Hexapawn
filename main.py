import random

currBoard = [
    2, 2, 2,
    0, 0, 0,
    1, 1, 1
]

AIprevMoves = []

def validateMove(playerMove):
    if playerMove not in possiblePlayerMoves:
        return False
    if currBoard[playerMove[0] - 1] != 1:
        return False
    if playerMove[1] == playerMove[0] - 3 and currBoard[playerMove[1] - 1] != 0:
        return False
    if playerMove[0] in [7, 4]:
        if playerMove[1] == playerMove[0] - 2 and currBoard[playerMove[1] - 1] != 2:
            return False
        elif playerMove[1] in [6, 3]:
            return False
    elif playerMove[0] in [8, 5]:
        if playerMove[1] == playerMove[0] - 4 and currBoard[playerMove[1] - 1] != 2:
            return False
        elif playerMove[1] == playerMove[0] - 2 and currBoard[playerMove[1] - 1] != 2:
            return False
        elif playerMove[1] == playerMove[0] - 1:
            return False
    else: # playerMove[0] in [9, 6]
        if playerMove[1] == playerMove[0] - 4 and currBoard[playerMove[1] - 1] != 2:
            return False
        elif playerMove[1] >= playerMove[0] - 2:
            return False
    return True

def printCurrBoard():
    print(currBoard[0], currBoard[1], currBoard[2])
    print(currBoard[3], currBoard[4], currBoard[5])
    print(currBoard[6], currBoard[7], currBoard[8])
    print('\n')

def initMatch():
    print('This is what each number move means in a board')
    print('1 2 3\n4 5 6\n7 8 9\n')
    print('This is what the board looks like right now:')
    global currBoard
    currBoard = [
        2, 2, 2,
        0, 0, 0,
        1, 1, 1
    ]
    printCurrBoard()
    global AIprevMoves
    AIprevMoves = []

def playerWon():
    print('\nTHE PLAYER WON!\n')
    print('AI gets smarter.\n')
    AImoves[AIprevMoves[-1].get('id') - 1]['moves'].remove(AIprevMoves[-1].get('move'))
    if not AImoves[AIprevMoves[-1].get('id') - 1]['moves']:
        AImoves[AIprevMoves[-2].get('id') - 1]['moves'].remove(AIprevMoves[-2].get('move'))
    initMatch()

def AIwon():
    print('\nTHE AI WON!\n')
    initMatch()

def main():
    initMatch()
    while True:
        playerMove = [int(i) for i in str(input('Enter Your Move:'))]

        if not validateMove(playerMove):
            print('Invalid input')
            continue

        currBoard[playerMove[0] - 1], currBoard[playerMove[1] - 1] = 0, 1

        print('\nYour Move:\n')
        printCurrBoard()

        for move in AImoves:
            if move.get('board') == currBoard:
                AImove = move

        if not AImove.get('moves'):
            playerWon()
            continue

        move = [int(i) for i in str(random.choice(AImove.get('moves')))]

        currBoard[move[0] - 1], currBoard[move[1] - 1] = 0, 2

        AIprevMoves.append({
            'id': AImove.get('id'),
            'move': int(''.join([str(n) for n in move]))
        })

        print('\nAI Move:\n')
        printCurrBoard()

        if 2 in currBoard[6:] or 1 not in currBoard:
            AIwon()
            continue

        for n in possiblePlayerMoves:
            if validateMove(n):
                break
        else:
            AIwon()
            continue

possiblePlayerMoves = [[7, 4], [7, 5], [8, 4], [8, 5], [8, 6], [9, 5], [9,  6], [4, 1], [4, 2], [5, 1], [5, 2], [5, 3], [6, 2], [6, 3]]

AImoves = [
    # AI's first moves:
    {'id': 1, 'moves': [24, 25, 36], 'board': [
        2, 2, 2,
        1, 0, 0,
        0, 1, 1
    ]},
    {'id': 2, 'moves': [14, 15, 35, 36], 'board': [
        2, 2, 2,
        0, 1, 0,
        1, 0, 1
    ]},
    {'id': 3, 'moves': [14, 25, 26], 'board': [
        2, 2, 2,
        0, 0, 1,
        1, 1, 0
    ]},
    #--------------------------------------------------------
    # AI's second moves:
    {'id': 4, 'moves': [36], 'board': [ # AI WINS
        2, 0, 2,
        1, 0, 0,
        0, 0, 1
    ]},
    {'id': 5, 'moves': [15, 35, 36, 47], 'board': [
        2, 0, 2,
        2, 1, 0,
        0, 0, 1
    ]},
    {'id': 6, 'moves': [47, 48], 'board': [ # AI WINS
        2, 0, 2,
        2, 0, 1,
        0, 1, 0
    ]},
    {'id': 7, 'moves': [15, 35, 36], 'board': [
        2, 0, 2,
        1, 1, 0,
        0, 1, 0
    ]},
    {'id': 8, 'moves': [], 'board': [ # PLAYER WINS
        2, 0, 2,
        1, 2, 1,
        0, 1, 0
    ]},
    {'id': 9, 'moves': [], 'board': [ # PLAYER WINS
        2, 1, 0,
        0, 0, 2,
        0, 1, 1
    ]},
    {'id': 10, 'moves': [15, 24], 'board': [
        2, 2, 0,
        1, 1, 2,
        0, 0, 1
    ]},
    {'id': 11, 'moves': [24, 25, 26], 'board': [
        2, 2, 0,
        1, 0, 1,
        0, 0, 1
    ]},
    {'id': 12, 'moves': [], 'board': [ # PLAYER WINS
        0, 2, 1,
        2, 0, 0,
        1, 0, 1
    ]},
    {'id': 13, 'moves': [26, 35], 'board': [
        0, 2, 2,
        2, 1, 1,
        1, 0, 0
    ]},
    {'id': 14, 'moves': [24, 36, 58, 59], 'board': [
        0, 2, 2,
        1, 2, 0,
        0, 0, 1
    ]},
    {'id': 15, 'moves': [35, 36], 'board': [
        0, 2, 2,
        0, 1, 0,
        0, 0, 1
    ]},
    {'id': 16, 'moves': [35, 36], 'board': [
        0, 2, 2,
        0, 1, 0,
        1, 0, 0
    ]},
    {'id': 17, 'moves': [26, 57, 58], 'board': [
        0, 2, 2,
        0, 2, 1,
        1, 0, 0
    ]},
    {'id': 18, 'moves': [24, 58, 59], 'board': [
        2, 2, 0,
        1, 2, 0,
        0, 0, 1
    ]},
    {'id': 19, 'moves': [14, 15], 'board': [
        2, 2, 0,
        0, 1, 0,
        0, 0, 1
    ]},
    {'id': 20, 'moves': [14, 15], 'board': [
        2, 2, 0,
        0, 1, 0,
        1, 0, 0
    ]},
    {'id': 21, 'moves': [14, 26, 57, 58], 'board': [
        2, 2, 0,
        0, 2, 1,
        1, 0, 0
    ]},
    {'id': 22, 'moves': [], 'board': [ # PLAYER WINS
        1, 2, 0,
        0, 0, 2,
        1, 0, 1
    ]},
    {'id': 23, 'moves': [24, 25, 26], 'board': [
        0, 2, 2,
        1, 0, 1,
        1, 0, 0
    ]},
    {'id': 24, 'moves': [], 'board': [ # PLAYER WINS
        0, 1, 2,
        2, 0, 0,
        1, 1, 0
    ]},
    {'id': 25, 'moves': [14, 15, 35], 'board': [
        2, 0, 2,
        0, 1, 1,
        0, 1, 0
    ]},
    {'id': 26, 'moves': [68, 69], 'board': [ # AI WINS
        2, 0, 2,
        1, 0, 2,
        0, 1, 0
    ]},
    {'id': 27, 'moves': [14, 15, 35, 69], 'board': [
        2, 0, 2,
        0, 1, 2,
        1, 0, 0
    ]},
    {'id': 28, 'moves': [14], 'board': [ # AI WINS
        2, 0, 2,
        0, 0, 1,
        1, 0, 0
    ]},
    #--------------------------------------------------------
    # AI's third moves:
    {'id': 29, 'moves': [35, 36, 47], 'board': [
        0, 0, 2,
        2, 1, 0,
        0, 0, 0
    ]},
    {'id': 30, 'moves': [47, 58], 'board': [ # AI WINS
        0, 0, 2,
        2, 2, 1,
        0, 0, 0
    ]},
    {'id': 31, 'moves': [15, 47], 'board': [ # AI WINS
        2, 0, 0,
        2, 1, 0,
        0, 0, 0
    ]},
    {'id': 32, 'moves': [47, 58], 'board': [ # AI WINS
        2, 0, 0,
        2, 2, 1,
        0, 0, 0
    ]},
    {'id': 33, 'moves': [], 'board': [ # PLAYER WINS
        1, 0, 0,
        2, 0, 2,
        0, 0, 1
    ]},
    {'id': 34, 'moves': [], 'board': [ # PLAYER WINS
        2, 1, 0,
        2, 0, 2,
        0, 0, 1
    ]},
    {'id': 35, 'moves': [], 'board': [ # PLAYER WINS
        1, 0, 2,
        0, 2, 0,
        0, 1, 0
    ]},
    {'id': 36, 'moves': [15], 'board': [
        2, 0, 0,
        1, 1, 1,
        0, 0, 0
    ]},
    {'id': 37, 'moves': [], 'board': [ # PLAYER WINS
        2, 1, 0,
        1, 0, 2,
        0, 1, 0
    ]},
    {'id': 38, 'moves': [], 'board': [ # PLAYER WINS
        1, 2, 0,
        0, 2, 2,
        0, 0, 1
    ]},
    {'id': 39, 'moves': [], 'board': [ # PLAYER WINS
        0, 1, 0,
        0, 2, 2,
        0, 0, 1
    ]},
    {'id': 40, 'moves': [24, 69], 'board': [
        0, 2, 0,
        1, 1, 2,
        0, 0, 0
    ]},
    {'id': 41, 'moves': [], 'board': [ # PLAYER WINS
        2, 0, 1,
        2, 0, 0,
        0, 0, 1
    ]},
    {'id': 42, 'moves': [], 'board': [ # PLAYER WINS
        2, 0, 1,
        1, 2, 0,
        0, 0, 1
    ]},
    {'id': 43, 'moves': [], 'board': [ # PLAYER WINS
        0, 0, 1,
        2, 0, 2,
        1, 0, 0
    ]},
    {'id': 44, 'moves': [], 'board': [ # PLAYER WINS
        0, 1, 2,
        2, 0, 2,
        1, 0, 0
    ]},
    {'id': 45, 'moves': [26, 47], 'board': [
        0, 2, 0,
        2, 1, 1,
        0, 0, 0
    ]},
    {'id': 46, 'moves': [], 'board': [ # PLAYER WINS
        0, 1, 0,
        2, 2, 0,
        1, 0, 0
    ]},
    {'id': 47, 'moves': [], 'board': [ # PLAYER WINS
        0, 2, 1,
        2, 2, 0,
        1, 0, 0
    ]},
    {'id': 48, 'moves': [], 'board': [ # PLAYER WINS
        0, 2, 0,
        0, 1, 0,
        0, 0, 0
    ]},
    {'id': 49, 'moves': [26, 58], 'board': [ # AI WINS
        0, 2, 0,
        0, 2, 1,
        0, 0, 0
    ]},
    {'id': 50, 'moves': [24, 58], 'board': [ # AI WINS
        0, 2, 0,
        1, 2, 0,
        0, 0, 0
    ]},
    {'id': 51, 'moves': [58, 69], 'board': [ # AI WINS
        0, 0, 2,
        1, 2, 2,
        0, 0, 0
    ]},
    {'id': 52, 'moves': [35, 69], 'board': [ # AI WINS
        0, 0, 2,
        0, 1, 2,
        0, 0, 0
    ]},
    {'id': 53, 'moves': [58, 69], 'board': [ # AI WINS
        2, 0, 0,
        1, 2, 2,
        0, 0, 0
    ]},
    {'id': 54, 'moves': [14, 15, 69], 'board': [
        2, 0, 0,
        0, 1, 2,
        0, 0, 0
    ]},
    {'id': 55, 'moves': [], 'board': [ # PLAYER WINS
        1, 0, 2,
        0, 2, 1,
        1, 0, 0
    ]},
    {'id': 56, 'moves': [35], 'board': [
        0, 0, 2,
        1, 1, 1,
        0, 0, 0
    ]},
    {'id': 57, 'moves': [], 'board': [ # PLAYER WINS
        1, 0, 2,
        0, 0, 2,
        1, 0, 0
    ]},
    {'id': 58, 'moves': [], 'board': [ # PLAYER WINS
        0, 1, 2,
        2, 0, 1,
        0, 1, 0
    ]},
    {'id': 59, 'moves': [], 'board': [ # PLAYER WINS
        0, 0, 1,
        2, 0, 1,
        0, 1, 0
    ]},
    {'id': 60, 'moves': [], 'board': [ # PLAYER WINS
        2, 0, 1,
        0, 2, 0,
        0, 1, 0
    ]},
    #--------------------------------------------------------
    # AI's fourth moves, AI's losing board:
    {'id': 61, 'moves': [], 'board': [
        0, 1, 0,
        2, 0, 2,
        0, 0, 0
    ]},
    {'id': 62, 'moves': [], 'board': [
        1, 0, 0,
        0, 2, 1,
        0, 0, 0
    ]},
    {'id': 63, 'moves': [], 'board': [
        0, 0, 1,
        1, 2, 0,
        0, 0, 0
    ]}
]

main()
