def lis_length(arr):
    nums = arr
    if not nums:
        # no numbers in the given list
        return 0
    tails = [0] * len(nums)
    length = 1  # Initialize the length of the LIS to 1
    #import nums[0] into tails[0] so there is the starting point
    tails[0] = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < tails[0]:
            # reinitialize the sequence with smaller start
            tails[0] = nums[i]
        elif nums[i] > tails[length - 1]:
            # while the number are crescendo , append them
            tails[length] = nums[i]
            length += 1
        else:
            # introduce new value at right position
            # this will sort the list from the smallest element to the end but not increase length - sort is crescendo
            left, right = 0, length - 1
            while left < right:
                mid = left + (right - left) // 2
                if tails[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = nums[i]
    return length
print( lis_length( [10,9,2,5,3,7,101,18] ) )
