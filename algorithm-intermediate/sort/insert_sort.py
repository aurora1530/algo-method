from typing import List


def insert_sort(nums: List[int]):
    for k in range(1, len(nums)):
        pos = k
        while pos != 0 and nums[pos-1] > nums[pos]:
            nums[pos-1], nums[pos] = nums[pos], nums[pos-1]
            pos -= 1
        print(*nums)


N = int(input())
A = list(map(int, input().split()))
insert_sort(A)
