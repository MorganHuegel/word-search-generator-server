
def checkAtIndex(row, col, word, puzzle):
    positions = []
    letterCount = 0
    #check horizontally (rightwards)
    while letterCount < len(word):
        if col + letterCount == len(puzzle):
            positions = []
            letterCount = 0
            break
        elif puzzle[row][col + letterCount] == word[letterCount]:
            positions.append({'rowNum': row, 'colNum': col + letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check horizontally (leftwards)
    while letterCount < len(word):
        if col - letterCount < 0:
            positions = []
            letterCount = 0
            break
        elif puzzle[row][col - letterCount] == word[letterCount]:
            positions.append({'rowNum': row, 'colNum': col - letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check vertically (downwards)
    while letterCount < len(word):
        if row + letterCount == len(puzzle):
            positions = []
            letterCount = 0
            break
        elif puzzle[row + letterCount][col] == word[letterCount]:
            positions.append({'rowNum': row + letterCount, 'colNum': col})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check vertically (upwards)
    while letterCount < len(word):
        if row - letterCount < 0:
            positions = []
            letterCount = 0
            break
        elif puzzle[row - letterCount][col] == word[letterCount]:
            positions.append({'rowNum': row - letterCount, 'colNum': col})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check diagonally (upwards, rightwards)
    while letterCount < len(word):
        if row - letterCount < 0 or col + letterCount == len(puzzle):
            positions = []
            letterCount = 0
            break
        elif puzzle[row - letterCount][col + letterCount] == word[letterCount]:
            positions.append({'rowNum': row - letterCount, 'colNum': col + letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check diagonally (downwards, rightwards)
    while letterCount < len(word):
        if row + letterCount == len(puzzle) or col + letterCount == len(puzzle):
            positions = []
            letterCount = 0
            break
        elif puzzle[row + letterCount][col + letterCount] == word[letterCount]:
            positions.append({'rowNum': row + letterCount, 'colNum': col + letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check diagonally (upwards, leftwards)
    while letterCount < len(word):
        if row - letterCount < 0 or col - letterCount < 0:
            positions = []
            letterCount = 0
            break
        elif puzzle[row - letterCount][col - letterCount] == word[letterCount]:
            positions.append({'rowNum': row - letterCount, 'colNum': col - letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check diagonally (downwards, leftwards)
    while letterCount < len(word):
        if row + letterCount == len(puzzle) or col - letterCount < 0:
            positions = []
            letterCount = 0
            break
        elif puzzle[row + letterCount][col - letterCount] == word[letterCount]:
            positions.append({'rowNum': row + letterCount, 'colNum': col - letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    return False





def solver(word, puzzle):
    for r, row in enumerate(puzzle):
        for c, letter in enumerate(row):
            foundIt = False
            if letter == word[0]: 
                foundIt = checkAtIndex(r, c, word, puzzle)
            if foundIt != False: 
                return foundIt
    return False
