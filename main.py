def main():
    input('test: ')

AImoves = [
    # AI's first moves:
    {'id': 1, 'moves': [24, 25, 36], 'board': [
        [2, 2, 2],
        [1, 0, 0],
        [0, 1, 1]
    ]},
    {'id': 2, 'moves': [14, 15, 35, 36], 'board': [
        [2, 2, 2],
        [0, 1, 0],
        [1, 0, 1]
    ]},
    {'id': 3, 'moves': [14, 25, 26], 'board': [
        [2, 2, 2],
        [0, 0, 1],
        [1, 1, 0]
    ]},
    #--------------------------------------------------------
    # AI's second moves:
    {'id': 4, 'moves': [36], 'board': [ # AI WINS
        [2, 0, 2], # 2 0 2 AI's previous move (24)
        [1, 0, 0], # 2 0 0
        [0, 0, 1]  # 0 1 1
    ]},
    {'id': 5, 'moves': [47, 15, 35, 36], 'board': [
        [2, 0, 2], # 2 0 2 AI's previous move (24)
        [2, 1, 0], # 2 0 0
        [0, 0, 1]  # 0 1 1
    ]},
    {'id': 6, 'moves': [47, 48], 'board': [ # AI WINS
        [2, 0, 2], # 2 0 2 AI's previous move (24)
        [2, 0, 1], # 2 0 0
        [0, 1, 0]  # 0 1 1
    ]},
    {'id': 7, 'moves': [15, 35, 36], 'board': [
        [2, 0, 2], # 2 0 2 AI's previous move (25)
        [1, 1, 0], # 1 2 0
        [0, 1, 0]  # 0 1 1
    ]},
    {'id': 8, 'moves': [], 'board': [ # PLAYER WINS
        [2, 0, 2], # 2 0 2 AI's previous move (25)
        [1, 2, 1], # 1 2 0
        [0, 1, 0]  # 0 1 1
    ]},
    {'id': 9, 'moves': [], 'board': [ # PLAYER WINS
        [2, 1, 0], # 2 2 0 AI's previous move (36)
        [0, 0, 2], # 1 0 2
        [0, 1, 1]  # 0 1 1
    ]},
    {'id': 10, 'moves': [15, 24], 'board': [
        [2, 2, 0], # 2 2 0 AI's previous move (36)
        [1, 1, 2], # 1 0 2
        [0, 0, 1]  # 0 1 1
    ]},
    {'id': 11, 'moves': [24, 25, 26], 'board': [
        [2, 2, 0], # 2 2 0 AI's previous move (36)
        [1, 0, 1], # 1 0 2
        [0, 0, 1]  # 0 1 1
    ]},
    {'id': 12, 'moves': [], 'board': [ # PLAYER WINS
        [0, 2, 1], # 0 2 2 AI's previous move (14)
        [2, 0, 0], # 2 1 0
        [1, 0, 1]  # 1 0 1
    ]},
    {'id': 13, 'moves': [26, 35], 'board': [
        [0, 2, 2], # 0 2 2 AI's previous move (14)
        [2, 1, 1], # 2 1 0
        [1, 0, 0]  # 1 0 1
    ]},
    {'id': 14, 'moves': [24, 58, 59, 36], 'board': [
        [0, 2, 2], # 0 2 2 AI's previous move (15)
        [1, 2, 0], # 0 2 0
        [0, 0, 1]  # 1 0 1
    ]},
    {'id': 15, 'moves': [35, 36], 'board': [
        [0, 2, 2], # 0 2 2 AI's previous move (15)
        [0, 1, 0], # 0 2 0
        [0, 0, 1]  # 1 0 1
    ]},
    {'id': 16, 'moves': [35, 36], 'board': [
        [0, 2, 2], # 0 2 2 AI's previous move (15)
        [0, 1, 0], # 0 2 0
        [1, 0, 0]  # 1 0 1
    ]},
    {'id': 17, 'moves': [57, 58, 26], 'board': [
        [0, 2, 2], # 0 2 2 AI's previous move (15)
        [0, 2, 1], # 0 2 0
        [1, 0, 0]  # 1 0 1
    ]},
    {'id': 18, 'moves': [24, 58, 59], 'board': [
        [2, 2, 0], # 2 2 0 AI's previous move (35)
        [1, 2, 0], # 0 2 0
        [0, 0, 1]  # 1 0 1
    ]},
    {'id': 19, 'moves': [14, 15], 'board': [
        [2, 2, 0], # 2 2 0 AI's previous move (35)
        [0, 1, 0], # 0 2 0
        [0, 0, 1]  # 1 0 1
    ]},
    {'id': 20, 'moves': [14, 15], 'board': [
        [2, 2, 0], # 2 2 0 AI's previous move (35)
        [0, 1, 0], # 0 2 0
        [1, 0, 0]  # 1 0 1
    ]},
    {'id': 21, 'moves': [14, 26, 57, 58], 'board': [
        [2, 2, 0], # 2 2 0 AI's previous move (35)
        [0, 2, 1], # 0 2 0
        [1, 0, 0]  # 1 0 1
    ]},
    {'id': 22, 'moves': [15, 24], 'board': [
        [2, 2, 0], # 2 2 0 AI's previous move (36)
        [1, 1, 2], # 0 1 2
        [0, 0, 1]  # 1 0 1
    ]},
    {'id': 23, 'moves': [], 'board': [ # PLAYER WINS
        [1, 2, 0], # 2 2 0 AI's previous move (36)
        [0, 0, 2], # 0 1 2
        [1, 0, 1]  # 1 0 1
    ]},
    {'id': 24, 'moves': [26, 35], 'board': [
        [0, 2, 2], # 0 2 2 AI's previous move (14)
        [2, 1, 1], # 2 0 1
        [1, 0, 0]  # 1 1 0
    ]},
    {'id': 25, 'moves': [24, 25, 26], 'board': [
        [0, 2, 2], # 0 2 2 AI's previous move (14)
        [1, 0, 1], # 2 0 1
        [1, 0, 0]  # 1 1 0
    ]},
    {'id': 26, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 2], # 0 2 2 AI's previous move (14)
        [2, 0, 0], # 2 0 1
        [1, 1, 0]  # 1 1 0
    ]},
    {'id': 27, 'moves': [], 'board': [ # PLAYER WINS
        [2, 0, 2], # 2 0 2 AI's previous move (25)
        [1, 2, 1], # 0 2 1
        [0, 1, 0]  # 1 1 0
    ]},
    {'id': 28, 'moves': [14, 15, 35], 'board': [
        [2, 0, 2], # 2 0 2 AI's previous move (25)
        [0, 1, 1], # 0 2 1
        [0, 1, 0]  # 1 1 0
    ]},
    {'id': 29, 'moves': [68, 69], 'board': [ # AI WINS
        [2, 0, 2], # 2 0 2 AI's previous move (26)
        [1, 0, 2], # 0 0 2
        [0, 1, 0]  # 1 1 0
    ]},
    {'id': 30, 'moves': [14, 15, 35, 69], 'board': [
        [2, 0, 2], # 2 0 2 AI's previous move (26)
        [0, 1, 2], # 0 0 2
        [1, 0, 0]  # 1 1 0
    ]},
    {'id': 31, 'moves': [14], 'board': [ # AI WINS
        [2, 0, 2], # 2 0 2 AI's previous move (26)
        [0, 0, 1], # 0 0 2
        [1, 0, 0]  # 1 1 0
    ]},
    #--------------------------------------------------------
    # AI's third moves:
    {'id': 32, 'moves': [47, 35, 36], 'board': [
        [0, 0, 2], # 0 0 2 AI's previous move (15) [47, 15, 35, 36]
        [2, 1, 0], # 2 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 33, 'moves': [47, 58], 'board': [ # AI WINS
        [0, 0, 2], # 0 0 2 AI's previous move (15) [47, 15, 35, 36]
        [2, 2, 1], # 2 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 34, 'moves': [47, 15], 'board': [ # AI WINS
        [2, 0, 0], # 2 0 0 AI's previous move (35) [47, 15, 35, 36]
        [2, 1, 0], # 2 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 35, 'moves': [47, 58], 'board': [ # AI WINS
        [2, 0, 0], # 2 0 0 AI's previous move (35) [47, 15, 35, 36]
        [2, 2, 1], # 2 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 36, 'moves': [], 'board': [ # PLAYER WINS
        [1, 0, 0], # 2 0 0 AI's previous move (36) [47, 15, 35, 36]
        [2, 0, 2], # 2 1 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 37, 'moves': [], 'board': [ # PLAYER WINS
        [2, 1, 0], # 2 0 0 AI's previous move (36) [47, 15, 35, 36]
        [2, 0, 2], # 2 1 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 38, 'moves': [], 'board': [ # PLAYER WINS
        [1, 0, 2], # 0 0 2 AI's previous move (15) [15, 35, 36]
        [0, 2, 0], # 1 2 0
        [0, 1, 0]  # 0 1 0
    ]},
    {'id': 39, 'moves': [15], 'board': [
        [2, 0, 0], # 2 0 0 AI's previous move (36) [15, 35, 36]
        [1, 1, 1], # 1 1 2
        [0, 0, 0]  # 0 1 0
    ]},
    {'id': 40, 'moves': [], 'board': [ # PLAYER WINS
        [2, 1, 0], # 2 0 0 AI's previous move (36) [15, 35, 36]
        [1, 0, 2], # 1 1 2
        [0, 1, 0]  # 0 1 0
    ]},
    {'id': 41, 'moves': [], 'board': [ # PLAYER WINS
        [1, 2, 0], # 0 2 0 AI's previous move (15) [15, 24]
        [0, 2, 2], # 1 2 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 42, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 0], # 0 2 0 AI's previous move (15) [15, 24]
        [0, 2, 2], # 1 2 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 43, 'moves': [24, 69], 'board': [
        [0, 2, 0], # 0 2 0 AI's previous move (15) [15, 24]
        [1, 1, 2], # 1 2 2
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 44, 'moves': [], 'board': [ # PLAYER WINS
        [1, 0, 0], # 2 0 0 AI's previous move (24) [15, 24]
        [2, 0, 2], # 2 1 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 45, 'moves': [], 'board': [ # PLAYER WINS
        [2, 1, 0], # 2 0 0 AI's previous move (24) [15, 24]
        [2, 0, 2], # 2 1 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 46, 'moves': [], 'board': [ # PLAYER WINS
        [2, 0, 1], # 2 0 0 AI's previous move (24) [24, 25, 26]
        [2, 0, 0], # 2 0 1
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 47, 'moves': [], 'board': [ # PLAYER WINS
        [2, 0, 1], # 2 0 0 AI's previous move (25) [24, 25, 26]
        [1, 2, 0], # 1 2 1
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 48, 'moves': [15], 'board': [
        [2, 0, 0], # 2 0 0 AI's previous move (25) [24, 25, 26]
        [1, 1, 1], # 1 2 1
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 49, 'moves': [], 'board': [ # PLAYER WINS
        [0, 0, 1], # 0 0 2 AI's previous move (26) [26, 35]
        [2, 0, 2], # 2 1 2
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 50, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 2], # 0 0 2 AI's previous move (26) [26, 35]
        [2, 0, 2], # 2 1 2
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 51, 'moves': [47, 26], 'board': [
        [0, 2, 0], # 0 2 0 AI's previous move (35) [26, 35]
        [2, 1, 1], # 2 2 1
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 52, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 0], # 0 2 0 AI's previous move (35) [26, 35]
        [2, 2, 0], # 2 2 1
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 53, 'moves': [], 'board': [ # PLAYER WINS
        [0, 2, 1], # 0 2 0 AI's previous move (35) [26, 35]
        [2, 2, 0], # 2 2 1
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 54, 'moves': [47, 58], 'board': [ # AI WINS
        [0, 0, 2], # 0 0 2 AI's previous move (24) [24, 58, 59, 36]
        [2, 2, 1], # 2 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 55, 'moves': [47, 35], 'board': [ # AI WINS
        [0, 0, 2], # 0 0 2 AI's previous move (24) [24, 58, 59, 36]
        [2, 1, 0], # 2 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 56, 'moves': [], 'board': [ # PLAYER WINS
        [1, 2, 0], # 0 2 0 AI's previous move (36) [24, 58, 59, 36]
        [0, 2, 2], # 1 2 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 57, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 0], # 0 2 0 AI's previous move (36) [24, 58, 59, 36]
        [0, 2, 2], # 1 2 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 58, 'moves': [24, 69], 'board': [
        [0, 2, 0], # 0 2 0 AI's previous move (36) [24, 58, 59, 36]
        [1, 1, 2], # 1 2 2
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 59, 'moves': [], 'board': [ # PLAYER WINS
        [0, 2, 0], # 0 2 0 AI's previous move (35) [35, 36]
        [0, 1, 0], # 0 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 60, 'moves': [58, 26], 'board': [ # AI WINS
        [0, 2, 0], # 0 2 0 AI's previous move (35) [35, 36]
        [0, 2, 1], # 0 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 61, 'moves': [24, 58], 'board': [ # AI WINS
        [0, 2, 0], # 0 2 0 AI's previous move (35) [35, 36]
        [1, 2, 0], # 0 2 0
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 62, 'moves': [], 'board': [ # PLAYER WINS
        [0, 2, 0], # 0 2 0 AI's previous move (35) [35, 36]
        [0, 1, 0], # 0 2 0
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 63, 'moves': [24, 69], 'board': [
        [0, 2, 0], # 0 2 0 AI's previous move (36) [35, 36]
        [1, 1, 2], # 0 1 2
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 64, 'moves': [58, 69], 'board': [ # AI WINS
        [0, 0, 2], # 0 0 2 AI's previous move (26) [57, 58, 26]
        [1, 2, 2], # 0 2 2
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 65, 'moves': [35, 69], 'board': [ # AI WINS
        [0, 0, 2], # 0 0 2 AI's previous move (26) [57, 58, 26]
        [0, 1, 2], # 0 2 2
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 66, 'moves': [47, 58], 'board': [ # AI WINS
        [2, 0, 0], # 2 0 0 AI's previous move (24) [24, 58, 59]
        [2, 2, 1], # 2 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 67, 'moves': [47, 15], 'board': [ # AI WINS
        [2, 0, 0], # 2 0 0 AI's previous move (24) [24, 58, 59]
        [2, 1, 0], # 2 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 68, 'moves': [26, 47], 'board': [
        [0, 2, 0], # 0 2 0 AI's previous move (14) [14, 15]
        [2, 1, 1], # 2 1 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 69, 'moves': [], 'board': [ # PLAYER WINS
        [0, 2, 0], # 0 2 0 AI's previous move (15) [14, 15]
        [0, 1, 0], # 0 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 70, 'moves': [58, 26], 'board': [ # AI WINS
        [0, 2, 0], # 0 2 0 AI's previous move (15) [14, 15]
        [0, 2, 1], # 0 2 0
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 71, 'moves': [24, 58], 'board': [ # AI WINS
        [0, 2, 0], # 0 2 0 AI's previous move (15) [14, 15]
        [1, 2, 0], # 0 2 0
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 72, 'moves': [], 'board': [ # PLAYER WINS
        [0, 2, 0], # 0 2 0 AI's previous move (15) [14, 15]
        [0, 1, 0], # 0 2 0
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 73, 'moves': [47, 26], 'board': [
        [0, 2, 0], # 0 2 0 AI's previous move (14) [14, 26, 57, 58]
        [2, 1, 1], # 2 2 1
        [0, 0, 0]  # 1 0 0
    ]},
    ]{'id': 74, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 0], # 0 2 0 AI's previous move (14) [14, 26, 57, 58]
        [2, 2, 0], # 2 2 1
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 75, 'moves': [], 'board': [ # PLAYER WINS
        [0, 2, 1], # 0 2 0 AI's previous move (14) [14, 26, 57, 58]
        [2, 2, 0], # 2 2 1
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 76, 'moves': [58, 69], 'board': [ # AI WINS
        [2, 0, 0], # 2 0 0 AI's previous move (26) [14, 26, 57, 58]
        [1, 2, 2], # 0 2 2
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 77, 'moves': [14, 15, 69], 'board': [
        [2, 0, 0], # 2 0 0 AI's previous move (26) [14, 26, 57, 58]
        [0, 1, 2], # 0 2 2
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 78, 'moves': [], 'board': [ # PLAYER WINS
        [1, 2, 0], # 0 2 0 AI's previous move (15) [15, 24]
        [0, 2, 2], # 1 2 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 79, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 0], # 0 2 0 AI's previous move (15) [15, 24]
        [0, 2, 2], # 1 2 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 80, 'moves': [24, 69], 'board': [
        [0, 2, 0], # 0 2 0 AI's previous move (15) [15, 24]
        [1, 1, 2], # 1 2 2
        [0, 0, 0]  # 0 0 1
    ]},
    {'id': 81, 'moves': [], 'board': [ # AI WINS
        [1, 0, 0], # 2 0 0 AI's previous move (24) [15, 24]
        [2, 0, 2], # 2 1 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 82, 'moves': [], 'board': [ # AI WINS
        [2, 1, 0], # 2 0 0 AI's previous move (24) [15, 24]
        [2, 0, 2], # 2 1 2
        [0, 0, 1]  # 0 0 1
    ]},
    {'id': 83, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 2], # 0 0 2 AI's previous move (26) [26, 35]
        [2, 0, 2], # 2 1 2
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 84, 'moves': [], 'board': [ # PLAYER WINS
        [0, 0, 1], # 0 0 2 AI's previous move (26) [26, 35]
        [2, 0, 2], # 2 1 2
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 85, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 0], # 0 2 0 AI's previous move (35) [26, 35]
        [2, 2, 0], # 2 2 1
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 86, 'moves': [], 'board': [ # PLAYER WINS
        [0, 2, 1], # 0 2 0 AI's previous move (35) [26, 35]
        [2, 2, 0], # 2 2 1
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 87, 'moves': [26, 47], 'board': [
        [0, 2, 0], # 0 2 0 AI's previous move (35) [26, 35]
        [2, 1, 1], # 2 2 1
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 88, 'moves': [], 'board': [ # PLAYER WINS
        [1, 0, 2], # 0 0 2 AI's previous move (25) [24, 25, 26]
        [0, 2, 1], # 1 2 1
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 89, 'moves': [35], 'board': [
        [0, 0, 2], # 0 0 2 AI's previous move (25) [24, 25, 26]
        [1, 1, 1], # 1 2 1
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 90, 'moves': [], 'board': [ # PLAYER WINS
        [1, 0, 2], # 0 0 2 AI's previous move (26) [24, 25, 26]
        [0, 0, 2], # 1 0 2
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 91, 'moves': [35], 'board': [
        [0, 0, 2], # 0 0 2 AI's previous move (14) [14, 15, 35]
        [1, 1, 1], # 2 1 1
        [0, 0, 0]  # 0 1 0
    ]},
    {'id': 92, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 2], # 0 0 2 AI's previous move (14) [14, 15, 35]
        [2, 0, 1], # 2 1 1
        [0, 1, 0]  # 0 1 0
    ]},
    {'id': 93, 'moves': [], 'board': [ # PLAYER WINS
        [0, 0, 1], # 0 0 2 AI's previous move (14) [14, 15, 35]
        [2, 0, 1], # 2 1 1
        [0, 1, 0]  # 0 1 0
    ]},
    {'id': 94, 'moves': [], 'board': [ # PLAYER WINS
        [2, 0, 1], # 2 0 0 AI's previous move (35) [14, 15, 35]
        [0, 2, 0], # 0 2 1
        [0, 1, 0]  # 0 1 0
    ]},
    {'id': 95, 'moves': [], 'board': [ # PLAYER WINS
        [0, 0, 1], # 0 0 2 AI's previous move (14) [14, 15, 35, 69]
        [2, 0, 2], # 2 1 2
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 96, 'moves': [], 'board': [ # PLAYER WINS
        [0, 1, 2], # 0 0 2 AI's previous move (14) [14, 15, 35, 69]
        [2, 0, 2], # 2 1 2
        [1, 0, 0]  # 1 0 0
    ]},
    {'id': 97, 'moves': [58, 69], 'board': [ # AI WINS
        [0, 0, 2], # 0 0 2 AI's previous move (15) [14, 15, 35, 69]
        [1, 2, 2], # 0 2 2
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 98, 'moves': [35, 69], 'board': [ # AI WINS
        [0, 0, 2], # 0 0 2 AI's previous move (15) [14, 15, 35, 69]
        [0, 1, 2], # 0 2 2
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 99, 'moves': [58, 69], 'board': [ # AI WINS
        [2, 0, 0], # 2 0 0 AI's previous move (35) [14, 15, 35, 69]
        [1, 2, 2], # 0 2 2
        [0, 0, 0]  # 1 0 0
    ]},
    {'id': 100, 'moves': [15, 69], 'board': [ # AI WINS
        [2, 0, 0], # 2 0 0 AI's previous move (35) [14, 15, 35, 69]
        [0, 1, 2], # 0 2 2
        [0, 0, 0]  # 1 0 0
    ]},
    #--------------------------------------------------------
    # AI's fourth moves, AI's losing board:
    {'id': 101, 'moves': [], 'board': [
        [0, 1, 0],
        [2, 0, 2]
        [0, 0, 0]
    ]},
    {'id': 102, 'moves': [], 'board': [
        [1, 0, 0],
        [0, 2, 1],
        [0, 0, 0]
    ]},
    {'id': 103, 'moves': [], 'board': [
        [0, 0, 1],
        [1, 2, 0],
        [0, 0, 0]
    ]}
]

main()
