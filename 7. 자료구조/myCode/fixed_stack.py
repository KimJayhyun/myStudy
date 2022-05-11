from typing import Any, Sequence

class FixedStack:
    class Empyty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity:int = 256) -> None:
        """초기화"""
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수를 반환"""
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value:Any) -> None:
        if self.is_full():
            raise FixedStack.Full

        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empyty
        self.ptr -= 1
        # del self.stk[self.ptr]
        return self.stk[self.ptr]
