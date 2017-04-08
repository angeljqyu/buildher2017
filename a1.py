"""Assignment 1.

Fill in the following function skeletons - descriptions are provided in the PDF,
and briefly in the docstring (the triple quote thing at the top of each function).

Some assert statements have been provided - write more of them to test your code!!"""

#########################
def absolute(n):
    """Takes a number, and returns the absolute value of that number.

    Cannot use the built in function `abs`."""
    if (n >= 0):
        return n
    if (n < 0):
        return n*(-1)

assert absolute(-1) == 1, "absolute of -1 failed"
assert absolute(0) == 0, "absolute of 0 failed"
assert absolute(5) == 5, "absolute of 5 failed"

#########################
def factorial(n):
    """Takes a number, and computes the factorial n!"""
    res = 1
    if (n == 0):
        return 1
    if (n == 1):
        return 1
    for x in range(1, (n+1)):
        res = res*x
    return res

assert factorial(3) == 6, "factorial of 3 failed"
assert factorial(4) == 24, "factorial of 4 failed"
assert factorial(0) == 1, "factorial of 0 failed"
assert factorial(1) == 1, "factorial of 1 failed"

#########################
def every_other(lst):
    """Takes a list, and returns a list of every other element 
    in the list, starting with the first."""
    return lst[::2]

assert every_other([1,2,3,4,5]) == [1,3,5], "every_other of [1,2,3,4,5] failed"
assert every_other([3,4,5,6,7,8]) == [3,5,7], "every_other of [3,4,5,6,7,8] failed"
assert every_other([1]) == [1], "every_other of [1] failed"
assert every_other([1,2]) == [1], "every_other of [1,2] failed"

#########################
def sum_list(lst):
    """Takes a list of numbers, and returns the sum of the numbers in that list."""
    res = 0
    for n in lst:
        res += n
    return res

assert sum_list([1,2,3]) == 6, "sum_list of [1,2,3] failed"
assert sum_list([1,3,4,5]) == 13, "sum_list of [1,3,4,5] failed"
assert sum_list([1]) == 1, "sum_list of [1] failed"
assert sum_list([]) == 0, "sum_list of [] failed"

#########################
def mean(lst):
    """Takes a list of numbers, and returns the mean of the numbers."""
    res = float(sum_list(lst))/float(len(lst))
    return float(res)

assert mean([1,2,3,4,5]) == 3, "mean of [1,2,3,4,5] failed"
assert mean([1,2,4,1]) == 2, "mean of [1,2,4,1] failed"
assert mean([1,3]) == 2, "mean of [1,3] failed"
assert mean([1,4]) == 2.5, "mean of [1,4] failed"

#########################
def median(lst):
    """Takes an ordered list of numbers, and returns the median of the numbers.
    If the list has an even number of values, it computes the mean of the two 
    center values."""
    lst = sorted(lst)
    if len(lst) < 1: 
        return 0
    if len(lst)%2 == 1:
        return lst[((len(lst)+1)/2)-1]
    else: 
        return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

assert median([1,2,3,4,5]) == 3, "median of [1,2,3,4,5] failed"
assert median([3,4,1,2,4,5]) == 3.5, "median of [3,4,1,2,4,5] failed"
assert median([1]) == 1, "median of [1] failed"
assert median([]) == 0, "median of [] failed"
assert median([1,6,5,4,2]) == 4, "median of [1,6,5,4,2] failed"

#########################
def duck_duck_goose(lst):
    """Given an list of names (strings), play 'duck duck goose' with it, knocking 
    out every third name (wrapping around) until only two names are left. In other 
    words, when you hit the end of the list, wrap around and keep counting from 
    where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd 
    first knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on 
    Nathan and 'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.
    
    You may assume the list has 3+ names to start."""
    index = 2
    while len(lst) > 2:
        del lst[index]
        index += 2
        if index > (len(lst)-1):
            index = index-len(lst)
    return lst

names = ["sasha", "nathan", "jennie", "shane", "will", "sara"]
assert duck_duck_goose(names) == ["sasha", "will"]
names1 = ["sasha", "nathan", "jennie", "shane", "will"]
assert duck_duck_goose(names1) == ["nathan", "shane"]
names2 = ["sasha", "nathan", "jennie", "shane"]
assert duck_duck_goose(names2) == ["sasha", "shane"]