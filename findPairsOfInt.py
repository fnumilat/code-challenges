# Find all the pairs of two integers in an unsorted array that sum up to a given S. 
# For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program 
# should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

## Understanding:
# I have an unsorted array.
# Given S which is an integer.
# My task is to find those pairs of 
# integers that sum up to the given S integer.

## Planning:
# I am going to create a function.
# Then going to loop through the first integer of the pair.
# And in a nested loop will loop through the second integer.
# Going to see if the sum of the first integer and second one
# is the given S, then will return them in an array and print.

## Execution:
def findPairsOfInt(array, sum):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == sum:
                newArray = [array[j], array[i]]
                print(newArray)

## Test Cases:
array = [3, 5, 2, -4, 8, 11]
sum = 7
findPairsOfInt(array, sum)
