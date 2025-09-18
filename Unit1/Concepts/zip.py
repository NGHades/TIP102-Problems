"""zip(x, y) takes two or more iterablues and returns a 
sequence of tuples where each the first item from eac iterable 
forms the first tuple in the sequence
"""

alphabet = ["a", "b", "c", "d"]
index = [1, 2, 3, 4, 5]
print(dict(zip(index, alphabet)))

zipped = zip(alphabet, index)
print(list(zipped))