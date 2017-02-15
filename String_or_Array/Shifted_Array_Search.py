"""If the sorted array arr is shifted left by an unknown offset and you don't have a pre-shifted copy of it,
 how would you modify your method to find a number in the shifted array?"""


def binarySearch(arr, num, begin, end):
    while begin <= end:
        mid = round((begin+end)/2)
        if arr[mid] < num:
            begin = mid + 1
        elif arr[mid] == num:
            return mid
        else:
            end = mid - 1
    return -1


def shiftedArrSearch(shiftArr, num):
    originalFirst = getOrigFirst(shiftArr)
    n = len(shiftArr)
    if shiftArr[originalFirst] <= num <= shiftArr[n-1]:
        return binarySearch(shiftArr, num, originalFirst, n - 1)
    else:
        return binarySearch(shiftArr, num, 0, originalFirst - 1)


def getOrigFirst(arr):
    begin = 0
    end = len(arr)-1
    while begin <= end:
        mid = int((begin+end)/2)
        if mid == 0 or arr[mid] < arr[mid-1]:
            return mid
        if arr[mid] > arr[0]:
            begin = mid + 1
        else:
            end = mid - 1
    return 0

if __name__ == '__main__':
    shiftArr = [9, 12, 17, 2, 4, 5]
    print(shiftedArrSearch(shiftArr, 4))
