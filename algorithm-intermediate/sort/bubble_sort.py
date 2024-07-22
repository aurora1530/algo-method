from typing import List


def bubble_sort(nums: List[int]):
    while True:
        is_updated = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                [nums[i], nums[i+1]] = [nums[i+1], nums[i]]
                is_updated = True
        if not is_updated:
            return
        print(' '.join(map(str, nums)))


N = int(input())
A = list(map(int, input().split()))

bubble_sort(A)
