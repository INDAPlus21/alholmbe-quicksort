import sys


def quicksort(nums, low, high):

    if low < high:
        l = low
        h = high
        p = nums[high]

        while (True):
            while (l < h) and (nums[l] <= p):
                l += 1
            while (h > l) and (nums[h] >= p):
                h -= 1
            if l < h:
                tmp = nums[l]
                nums[l] = nums[h]
                nums[h] = tmp

            if l >= h:
                break

        nums[high] = nums[l]
        nums[l] = p

        quicksort(nums, low, l - 1)
        quicksort(nums, l+1, high)


if __name__ == '__main__':
    for line in sys.stdin:
        nums = [int(elem) for elem in line.split()][1:]
    quicksort(nums, 0, len(nums)-1)

    for num in nums:
        print(num, end=' ')
