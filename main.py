import sys


def help_func(front, end):
    if front >= end:
        return
    left, right = front, end
    m = (right - left) // 2 + left
    pivot = nums[m]
    while right >= left:
        while right >= left and nums[left] < pivot:
            left += 1
        while right >= left and nums[right] > pivot:
            right -= 1
        if right >= left:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    help_func(front, right)
    help_func(left, end)


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
