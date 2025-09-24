def find_duplicate_chests(chests):
    # Understand
    #     Inputs
    #     Outputs
    #     Constraints
    #     Edge Cases
    # Plan
    # Implement

    duplicates = []
    for i in range(len(chests)):
        for j in range(i + 1, len(chests)):
            if chests[i] == chests[j]:
                duplicates.append(chests[i])
    return sorted(duplicates)
# Example
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

# Expected Output
# [2, 3]
# [1]
# []