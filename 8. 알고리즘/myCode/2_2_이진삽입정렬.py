from typing import MutableSequence

def binary_insertion_sort(data : MutableSequence):
    length = len(data)

    for i in range(1, length):    
        key = data[i]
        pl = 0 # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1 # 검색 범위의 맨 끝 원소 인덱스

        while True:
            pc = (pl + pr) // 2 # 검색할 원소 인덱스
            if data[pc] == key:
                break
            elif data[pc] < key:
                pr = pc - 1
            else : 
                pl = pc + 1

            if pl > pr:
                break
        
        # 삽입할 위치의 인덱스
        pd = pc + 1 if pl <= pr else pr + 1 

        for j in range(i, pd, -1):
            data[j] = data[j - 1]
        data[pd] = key
        