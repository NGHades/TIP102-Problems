def find_balanced_subsequence(art_pieces):
    # Understand

    # Plan
    # Make frequency map of art_pieces
    # loop through
    # if key + 1 in art_pieces
    # max = max(maximum, value + art_pieces[key + 1])
    # Implement

    art_map = {}
    for i in art_pieces:
        if i in art_map:
            art_map[i] += 1
        else:
            art_map[i] = 1

    maximum = 0
    for key, value in art_map.items():
        if key + 1 in art_map:
            maximum = max(maximum, value + art_map[key + 1])
    return maximum

    

art_pieces1 = [1,3,2,2,5,2,3,7]
print(find_balanced_subsequence(art_pieces1))
