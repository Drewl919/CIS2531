##Program: Grade Processing
##Name: Andrew Musielak
## Date: 07.12.2021
# Reads in grades from files and generates a report
#-------------------------------------------------------------#

def displayScores(scoreArray):
    """Displays the current test scores"""
    print("The current test scores are:")
    for i in range(len(scoreArray)-1):
        print(float(scoreArray[i]), end= "%, ")
    print(float(scoreArray[len(scoreArray)-1]), end = "%\n")


def findMin(scoreArray):
    """Finds the minimum value in list passed by parameter"""
    lowest = 100
    for value in scoreArray:
        current = value
        if current < lowest:
            lowest = current
    return lowest


def findMax(scoreArray):
    """Finds the maximum value in list passed by parameter"""
    highest = 0
    for value in scoreArray:
        current = value
        if current > highest:
            highest = current
    return highest


def dropLowest(scoreArray):
    """Calls findMin and removes the value that is returned"""
    lowest = findMin(scoreArray)
    scoreArray.remove(lowest)
    return scoreArray


def getMean(scoreArray):
    """Finds the average value in list passed by parameter"""
    count = 0
    total = 0
    for value in scoreArray:
        total += value
    average = total/len(scoreArray)
    return average


def findMedian(scoreArray):
    """Finds the median value in list passed by parameter"""
    scoreArray.sort(reverse=True)
    if len(scoreArray) % 2 == 1:
        median = scoreArray[int(len(scoreArray)/2)]
    else:
        median = (scoreArray[int(len(scoreArray)/2)]+scoreArray[int(len(scoreArray)/2)-1])/2
    return median


def getScores():
    """Reads scores from "scores.txt" and inserts it in the list"""
    file = open("scores.txt", "r")
    scores = []
    value = file.readline()
    while value != "":
        scores.append(int(value))
        value = file.readline()
    file.close()
    return scores


def saveScores(scoreArray):
    """Saves scores to "scores.text" from list passed by parameter"""
    file = open("updatedScores.txt", "w")
    for value in scoreArray:
        file.write(str(value) + "\n")
    file.close()


def main():
    testScores = getScores()
    # testScores = [90,85,52,74,95,100,78]
    displayScores(testScores)
    print()
    minimum = findMin(testScores)
    print("Lowest Score: ", minimum)
    maximum = findMax(testScores)
    print("Highest Score: ", maximum)
    average = getMean(testScores)
    print("Average: ", average)
    median = findMedian(testScores)
    print("Median: ", median)

    testScores = dropLowest(testScores)
    print("\nAfter dropping the lowest score.")
    displayScores(testScores)
    average = getMean(testScores)
    print("Average: ", average)
    median = findMedian(testScores)
    print("Median: ", median)
    saveScores(testScores)


main()

