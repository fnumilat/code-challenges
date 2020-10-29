# Given an array of integers, find the sum of its elements.
# For example, if the array ar = [1,2,3], 1 + 2 + 3 = 6, so return 6.

#
# Complete the simpleArraySum function below.
#

## Understanding:
# I have an array of integers.
# My task is to find the sum of its elements.

## Planning:
# Loop through the elements of the array.
# Then increment them by each other and return the
# result of the increments.

## Executing:
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    increment = 0
    for element in ar:
        increment += element
    return(increment)

ar = [1,2,3]
invoked = simpleArraySum(ar)
print(invoked)
