def bucket_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    bucket = [None]*(max_num+1-min_num)

    for v in arr:
        bucket[v - min_num] = v

    list = []
    for v in bucket:
        if v is not None:
            list.append(v)

    return list


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert bucket_sort(arr) == [0, 3, 5, 8, 9, 10,
                                12, 14, 18, 20, 23, 35, 40, 60, 90, 95]
