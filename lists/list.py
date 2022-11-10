#!/usr/bin/python3

nums = [1,2,5,7,8]

target = 3

def twoSum(nums, target):
    prevMap = {} # val : index
    for i, n in enumerate(nums):
        if target - n in prevMap:
            return [prevMap[target - n], i]
        prevMap[n] = i

result = twoSum(nums, target)
print(result)