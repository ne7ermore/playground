import math


def jump_search(arr, target):
    len_a = len(arr)
    jump = int(math.sqrt(len_a))
    step = 0

    while step*jump < len_a and target > arr[step*jump]:
        step += 1

    distance = min(len_a-1-(step-1)*jump, jump)
    for i in range(distance):
        if target == arr[(step-1)*jump+1+i]:
            return (step-1)*jump+1+i

    return -1


if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    target = 144

    assert jump_search(arr, target) == 12
