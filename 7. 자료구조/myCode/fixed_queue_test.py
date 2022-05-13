from enum import Enum
from queue import Empty
from sys import breakpointhook
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])

def select_menu():
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep="   ", end=" ")

        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)


q = FixedQueue(64)
for i in range(1, 6):
    q.enque(i)

while True:
    print(f'현재 데이터 개수 : {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input('인큐할 데이터를 입력하세요 : '))
        try :
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 가득 참')  

    elif menu == Menu.디큐:
        try :
            x = q.deque()
            print(f'디큐한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print('큐가 비었음')

    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f"피크한 데이터는 {x}")
        except FixedQueue.Empty:
            print('큐가 비었음')

    elif menu == Menu.검색:
        x = int(input('검색할 값을 입력하세요 : '))
        try:
            if q.find(x) >= 0 :
                print(f'{q.count(x)}개가 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')
            else :
                # q.find(x) == -1 
                print('입력 값이 없습니다.')
        except FixedQueue.Empty:
            print('큐가 비었음')

    elif menu == Menu.덤프:
        q.dump()
    
    else :
        break


