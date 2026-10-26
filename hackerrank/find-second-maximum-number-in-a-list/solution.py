if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))

arr_to_set=sorted(list(arr))
print(arr_to_set[-2])
