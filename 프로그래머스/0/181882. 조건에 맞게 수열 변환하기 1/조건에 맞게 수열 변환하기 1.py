def solution(arr):
    for i in range(len(arr)):
        num = arr[i]
        if num < 50 and num % 2 != 0:
            arr[i] *= 2
        elif num >= 50 and num % 2 == 0:
            arr[i] /= 2
            
    return arr