from typing import List


def zhongweishu(nums: List[int]):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2-1] + nums[n // 2]) / 2
nums=[2,3]
print(zhongweishu(nums))