def shell_sort(data):
    n = len(data)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = data[i]

            while j >= 0 and data[j] > tmp:
                data[j + h] = data[j]
                j -= h
                data[j+h] = tmp
        h //= 2

data = [4, 2, 3, 5, 6]
shell_sort(data)
print(data)
            