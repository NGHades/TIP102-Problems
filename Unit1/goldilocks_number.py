def goldilocks_approved(nums):
    # returns any number from the list that is neither min or max, 
    # or -1 if there isn't any of those

    # Edge Cases
    # 1. if list is less than 3
    # 2. elif min == max
    
    # # Steps
    # 1. if list is less than 3, return -1
    # 2. declare min, max
    # 3. declare mt_lst
    # 4. for loop through nums list
    #     if element != min and element != max
    #         append to mt_lst
    #         or 
    #         return element
    # Q. in this example, only return a single number

    if len(nums) < 3:
        return -1
    minNum = min(nums)
    maxNum = max(nums)
    mt_lst = []
    for i in nums:
        if i != min and i != max:
            return i

# Example Usage
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))

# Expected Output
"""
2
-1
2
"""