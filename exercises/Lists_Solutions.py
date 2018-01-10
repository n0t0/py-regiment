### Exercise 1
# Write a function called nested_sum that takes a nested list of integers and
# add up the elements from all of the nested lists.

# Sometimes you want to traverse one list while building another.
# For example, the following function takes a list of strings and returns
# a new list that contains capitalized strings:

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


# res is initialized with an empty list; each time through the loop, we append
# the next element. So res is another kind of accumulator.

# An operation like _capitalize_all_ is sometimes called a map because it
# "maps" a function (in this case the method capitalize) onto each of the
# elements in a sequence.


def nested_sum(list):
    pass
