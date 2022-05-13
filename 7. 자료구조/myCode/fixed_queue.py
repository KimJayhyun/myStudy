from typing import Any

class FixedQueue():
    class Empty(Exception):
        """Queue가 비어있음"""
        pass
    
    class Full(Exception):
        """Queue가 가득 찼음"""
        pass

    def __init__(self, capacity) -> None:
        self.no = 0 # 현재 데이터 개수
        self.front = 0 # 맨 앞 원소의 커서 위치
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        """큐의 데이터 개수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, data):
        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear] = data
        self.rear += 1
        self.no += 1
        
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty

        data = self.que[self.front]
        self.front += 1
        self.no -= 1
        
        if self.front == self.capacity:
            self.front = 0

        return data

    def peek(self) -> Any:
        """데이터를 피크"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value) -> int:
        """value를 찾아 인덱스를 반환하고 없으면 -1을 반환"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value) -> int:
        """큐에 포함되어 있는 value의 개수 반환"""
        count = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                count += 1
        
        return count

    def __contain__(self, value) -> bool:
        return self.count(value) > 0

    def clear(self) -> None:
        """큐를 초기화"""
        self.no = self.front = self.rear = 0

    def dump(self):
        """모든 데이터를 맨 앞에서 맨 끝 순서로 출력합니다."""
        if self.is_empty():
            raise FixedQueue.Empty
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity
                print(self.que[idx], end =" ")
            print()
        
