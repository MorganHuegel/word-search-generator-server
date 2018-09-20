#INPUT: List of words
# (words longer than 5 letters increase the chance that a word-search cannot mathematically be created)

#output: 2-dimensional matrix, 10x10, where the words are displayed horizontally or vertically (NO DIAGONAL)
# Example output:
filledArray = [
    ['a', "d", "o", "g", 'f', 'q', "e", 'm', 'a', 'o'],
    ['r', 'h', 'a', 'g', 'f', 'q', "a", 'l', 'h', 'p'],
    ['s', 'l', 'y', 'o', 'f', 'q', "g", 'e', 'u', 'v'],
    ['p', 'i', 'a', 'g', 'f', 'q', "l", 't', 'u', 'b'],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
    ['' for i in range(10)], #row not filled for testing purposes
    ['' for i in range(10)], #row not filled for testing purposes
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
]


# Approach:
# 1. loop through words array, looking at one word at a time (i.e. 'dog')
# 2. randomly select horizontal, vertical, or diagonal (random number 1-3)
# 3. if horizontal, run horizontal function:
#   - if it returns False, try running the vertical function on that word instead
# 4. if vertical, run vertical function:
#   - if it returns False, try running the diagonal function on that word instead
# 5. if diagonal, run the diagonal function:
#   - if it returns False, try running the horizontal function
# 6. keep counter to ensure that it only tries each method once for each word
#   - return False if each direction has been tried with no luck
# 7. after each word has been inserted, loop through results Array, replacing '' with random letter
# 8. return the results Array





import random
import string
import pprint


alphabet = string.ascii_lowercase



def horizontalAssign(word, resultsArray):
    puzzleWidth = len(resultsArray)
    wordLength = len(word)

    rowIndex = random.randint(0, puzzleWidth - 1)
    forward = random.randint(0, 1)
    if forward:
        # makes sure you're not too close to the right side
        columnIndex = random.randint(0, puzzleWidth - wordLength)

        i = 0
        rowSwitches = 0
        columnSwitches = 0
        while i < wordLength:
            if(rowSwitches == puzzleWidth and columnSwitches == (puzzleWidth + 1 - wordLength)):
                # no where for the word to fit
                return False
            elif rowSwitches == puzzleWidth:
                # no rows available for that column index, so switch columns
                rowSwitches = 0
                columnIndex = (columnIndex - 1) % (puzzleWidth + 1 - wordLength)
                columnSwitches += 1

            checkValue = resultsArray[rowIndex][columnIndex + i]
            if (checkValue == '' or checkValue == word[i]):
                i += 1
            else:
                # if the spots are already taken, check the next row
                rowIndex = (rowIndex + 1) % puzzleWidth
                rowSwitches += 1
                i = 0

        #should have correct rowIndex, colIndex by this point
        for j, letter in enumerate(word):
            resultsArray[rowIndex][columnIndex + j] = letter
        
    
    else:
        # make sure you're not too close to the left side
        columnIndex = random.randint(wordLength - 1, puzzleWidth - 1)

        i = 0
        rowSwitches = 0
        columnSwitches = 0
        while i < wordLength:
            if(rowSwitches == puzzleWidth and columnSwitches == (puzzleWidth + 1 - wordLength)):
                # no where for the word to fit
                return False
            elif rowSwitches == puzzleWidth:
                # no rows available for that column index, so try next column
                rowSwitches = 0
                columnIndex = columnIndex + 1
                if columnIndex == puzzleWidth:
                    columnIndex = wordLength - 1
                columnSwitches += 1

            checkValue = resultsArray[rowIndex][columnIndex - i]
            if (checkValue == '' or checkValue == word[i]):
                i += 1
            else:
                # if the spots are already taken, check the next row
                rowIndex = (rowIndex + 1) % puzzleWidth
                rowSwitches += 1
                i = 0

        #should have correct rowIndex and columnIndex by this point
        for j, letter in enumerate(word):
            resultsArray[rowIndex][columnIndex - j] = letter
    
    return resultsArray








def verticalAssign(word, resultsArray):
    puzzleWidth = len(resultsArray)
    wordLength = len(word)

    columnIndex = random.randint(0, puzzleWidth - 1)
    readDownwards = random.randint(0, 1)
    if readDownwards:
        # makes sure you're not too close to the bottom
        rowIndex = random.randint(0, puzzleWidth - wordLength)

        i = 0
        rowSwitches = 0
        columnSwitches = 0
        while i < wordLength:
            if(columnSwitches == puzzleWidth and rowSwitches == (puzzleWidth + 1 - wordLength)):
                # nowhere for the word to fit
                return False
            elif columnSwitches == puzzleWidth:
                # no columns available for that row index, so switch rows
                columnSwitches = 0
                rowIndex = (rowIndex + 1) % (puzzleWidth + 1 - wordLength)
                rowSwitches += 1

            checkValue = resultsArray[rowIndex + i][columnIndex]
            if (checkValue == '' or checkValue == word[i]):
                i += 1
            else:
                # if the spots are already taken, check the next column
                columnIndex = (columnIndex + 1) % puzzleWidth
                columnSwitches += 1
                i = 0

        #should have correct rowIndex and columnIndex by this point
        for j, letter in enumerate(word):
            resultsArray[rowIndex + j][columnIndex] = letter
    
    else:
        # make sure you're not too close to the top
        rowIndex = random.randint(wordLength - 1, puzzleWidth - 1)

        i = 0
        rowSwitches = 0
        columnSwitches = 0
        while i < wordLength:
            if(columnSwitches == puzzleWidth and rowSwitches == (puzzleWidth + 1 - wordLength)):
                # no where for the word to fit
                return False
            elif columnSwitches == puzzleWidth:
                # no rows available for that column index, so try next column
                columnSwitches = 0
                rowIndex = rowIndex + 1
                if rowIndex == puzzleWidth:
                    rowIndex = wordLength - 1
                rowSwitches += 1

            checkValue = resultsArray[rowIndex - i][columnIndex]
            if (checkValue == '' or checkValue == word[i]):
                i += 1
            else:
                # if the spots are already taken, check the next row
                columnIndex = (columnIndex + 1) % puzzleWidth
                columnSwitches += 1
                i = 0

        #should have correct rowIndex and columnIndex by this point
        for j, letter in enumerate(word):
            resultsArray[rowIndex - j][columnIndex] = letter
    
    return resultsArray








def diagonalAssign(word, resultsArray):
    puzzleWidth = len(resultsArray)
    wordLength = len(word)
    directionIndicator = random.randint(1, 4)

    if directionIndicator == 1:
        #reads top-to-bottom, left-to-right \
        rowIndex = random.randint(0, puzzleWidth - wordLength)
        columnIndex = random.randint(0, puzzleWidth - wordLength)

        i = 0
        columnSwitch = 0
        rowSwitch = 0
        while(i < len(word)):
            if(columnSwitch == puzzleWidth + 1 - wordLength and rowSwitch == puzzleWidth + 1 - wordLength):
                return False
            if(columnSwitch == puzzleWidth + 1 - wordLength):
                columnSwitch = 0
                rowIndex = (rowIndex + 1) % (puzzleWidth + 1 - wordLength)
                rowSwitch += 1

            checkValue = resultsArray[rowIndex + i][columnIndex + i]
            if (checkValue == '' or checkValue == word[i]):
                i += 1
            else:
                columnIndex = (columnIndex + 1) % (puzzleWidth + 1 - wordLength)
                columnSwitch += 1
                i = 0

        for j, letter in enumerate(word):
            resultsArray[rowIndex + j][columnIndex + j] = letter

    elif directionIndicator == 2:
        #reads top-to-bottom, right-to-left /
        rowIndex = random.randint(0, puzzleWidth - wordLength)
        columnIndex = random.randint(wordLength - 1, puzzleWidth - 1)

        i = 0
        rowsChecked = 0
        columnsChecked = 0
        while i < wordLength:
            if(rowsChecked == puzzleWidth + 1 - wordLength and columnsChecked == puzzleWidth + 1 - wordLength):
                return False
            elif(rowsChecked == puzzleWidth + 1 - wordLength):
                rowsChecked = 0
                columnIndex = columnIndex + 1
                if columnIndex > len(resultsArray) - 1:
                    columnIndex = wordLength - 1
                columnsChecked += 1

            checkValue = resultsArray[rowIndex + i][columnIndex - i]
            if (checkValue == '' or checkValue == word[i]):
                i += 1
            else:
                rowIndex = (rowIndex + 1) % (puzzleWidth + 1 - wordLength)
                rowsChecked += 1
                i = 0
        
        for j, letter in enumerate(word):
            resultsArray[rowIndex + j][columnIndex - j] = letter

    elif directionIndicator == 3:
        #reads bottom-to-top, right-to-left \
        rowIndex = random.randint(wordLength - 1, puzzleWidth - 1)
        columnIndex = random.randint(wordLength - 1, puzzleWidth - 1)

        i = 0
        rowsChecked = 0
        columnsChecked = 0
        while i < wordLength:
            if(rowsChecked == puzzleWidth + 1 - wordLength and columnsChecked == puzzleWidth + 1 - wordLength):
                return False
            elif(rowsChecked == puzzleWidth + 1 - wordLength):
                rowsChecked = 0
                columnIndex = columnIndex + 1
                if columnIndex > puzzleWidth - 1:
                    columnIndex = wordLength - 1
                columnsChecked += 1

            checkValue = resultsArray[rowIndex - i][columnIndex - i]
            if (checkValue == '' or checkValue == word[i]):
                i += 1
            else:
                rowIndex += 1
                if rowIndex > puzzleWidth - 1:
                    rowIndex = wordLength - 1
                rowsChecked += 1
                i = 0
        
        for j, letter in enumerate(word):
            resultsArray[rowIndex - j][columnIndex - j] = letter

    else:
        #reads bottom-to-top, left-to-right /
        rowIndex = random.randint(wordLength - 1, puzzleWidth - 1)
        columnIndex = random.randint(0, puzzleWidth - wordLength)

        i = 0
        rowsChecked = 0
        columnsChecked = 0
        while i < wordLength:
            if(rowsChecked == puzzleWidth + 1 - wordLength and columnsChecked == puzzleWidth + 1 - wordLength):
                return False
            elif(rowsChecked == puzzleWidth + 1 - wordLength):
                rowsChecked = 0
                columnIndex = (columnIndex + 1) % (puzzleWidth + 1 - wordLength)
                columnsChecked += 1

            checkValue = resultsArray[rowIndex - i][columnIndex + i]
            if (checkValue == '' or checkValue == word[i]):
                i += 1
            else:
                rowIndex += 1
                if rowIndex > puzzleWidth - 1:
                    rowIndex = wordLength - 1
                rowsChecked += 1
                i = 0
        
        for j, letter in enumerate(word):
            resultsArray[rowIndex - j][columnIndex + j] = letter

    return resultsArray








def generateWordSearchEasy(wordList, width):
    #make sure each word is shorter than the width:
    for word in wordList:
        if len(word) > width: return False

    resultMatrix = [['' for i in range(width)] for i in range(width)]
    for word in wordList:
        direction = random.randint(1,2)

        impossible = True
        attempts = 1
        while attempts <= 2:
            if direction == 1:
                if horizontalAssign(word, resultMatrix):
                    impossible = False
                    break
                else:
                    attempts += 1
                    direction = 2
            else:
                if verticalAssign(word, resultMatrix):
                    impossible = False
                    break
                else:
                    attempts += 1
                    direction = 1
        if impossible: return False  # means that the word could not be inserted anywhere in the puzzle, prompt user to try again

    for rowIndex, row in enumerate(resultMatrix):
        for colIndex, letter in enumerate(row):
            if letter == '':
                resultMatrix[rowIndex][colIndex] = alphabet[random.randint(0, 25)]
    return resultMatrix




def generateWordSearchHard(wordList, width):
    #make sure each word is shorter than the width:
    for word in wordList:
        if len(word) > width: return False

    resultMatrix = [['' for i in range(width)] for i in range(width)]

    for word in wordList:
        direction = random.randint(1,3)

        impossible = True
        attempts = 1
        while attempts < 4 :
            if direction == 1:
                if horizontalAssign(word, resultMatrix):
                    impossible = False
                    break
                else:
                    attempts += 1
                    direction = 2
            elif direction == 2:
                if verticalAssign(word, resultMatrix):
                    impossible = False
                    break
                else:
                    attempts += 1
                    direction = 3
            else:
                if diagonalAssign(word, resultMatrix):
                    impossible = False
                    break
                else:
                    attempts += 1
                    direction = 1
        if impossible: return False #means that the word could not be inserted in any direction, prompt user to try again

    for rowIndex, row in enumerate(resultMatrix):
        for colIndex, letter in enumerate(row):
            if letter == '':
                resultMatrix[rowIndex][colIndex] = alphabet[random.randint(0, 25)]
    return resultMatrix


# result = generateWordSearchEasy(['chimp', 'harry', 'alfred', 'heart', 'dog', 'zzzzz'], 10)
# pprint.pprint(result)
# ^^^^^ For checking the easy function ^^^^^


# pprint.pprint( generateWordSearchHard(['chimp', 'harry', 'alfred', 'heart', 'dog', 'zzzzz'], 15) )
# ^^^^^ For checking the hard function ^^^^^


# pprint.pprint( generateWordSearchHard(['chimpanzee', 'harrypotter', 'alfredosauce', 'heartthrob', 'dogandcats', 'zzzzzzzzzz'], 8) )
# ^^^^^ For checking the error case ^^^^^
