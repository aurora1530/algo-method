# 選択ソート
from typing import List


def min_idx(nums: List[int]) -> int:
    idx = -1
    m = 1001
    for i in range(len(nums)):
        if nums[i] < m:
            m = nums[i]
            idx = i
    return idx


def select_sort(nums: List[int]):
    for k in range(len(nums)-1):
        min_i = min_idx(nums[k:]) + k
        nums[k], nums[min_i] = nums[min_i], nums[k]
        print(*nums)


N = int(input())
A = list(map(int, input().split()))
select_sort(A)
