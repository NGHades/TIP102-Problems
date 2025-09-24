def total_treasures(treasure_map):
    sum = 0
    for i in treasure_map:
        sum += treasure_map[i]
    return sum

# Example
treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

from collections import Counter
def can_make_balanced(code):
    ctr = Counter(code)

    ctrMax = max(ctr.values())
    ctrMin = min(ctr.values())

    if (ctrMax- 1) == ctrMin:
        return True
    return False

# Example 
code1 = "arghhh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 

# Output
# True
# False