import sys


def help_func(head, tail):
    if head >= tail:
        return
    l, r = head, tail
    m = (r - l) // 2 + l
    pivot = nums[m]
    while r >= l:
        while r >= l and nums[l] < pivot:
            l += 1
        while r >= l and nums[r] > pivot:
            r -= 1
        if r >= l:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    help_func(head, r)
    help_func(l, tail)


def quicksort(nums):
    help_func(0, len(nums)-1)
    return nums


if __name__ == '__main__':
    nums = []
    for line in sys.stdin:
        nums = [int(elem) for elem in line.split()][1:]
    nums = quicksort(nums)
    for num in nums:
        print(num, end=' ')
