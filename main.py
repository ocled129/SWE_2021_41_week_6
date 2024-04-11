from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if(nums[i] + nums[j] == target):
                result.append(i)
                result.append(j)
                return result
            
# test
nums = []
for n in map(int, input().split()): nums.append(n)

target = int(input())

print(f"Input: nums = {nums}, target = {target}")
print(f"Output: {twoSum(nums, target)}")