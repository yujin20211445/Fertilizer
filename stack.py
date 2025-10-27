# 클래스 구조
class Stack:
    # 초기값
    def __init__(self, max_size=10):
        self.items = []
        self.max_size = max_size

    # 비료 추가(push)
    def push(self, item):
        try:
            item = int(item)
        except ValueError:
            print('숫자만 입력할 수 있습니다.')
            return

        # 스택 크기 확인
        if len(self.items) >= self.max_size:
            print('비료가 가득 찼습니다. 더 이상 추가할 수 없습니다.')
            return

        # 추가할거야?
        confirm = input(f'비료 {item}개를 추가하시겠습니까? (y/n): ')
        if confirm.lower() != 'y':
            print('추가 취소.')
            return

        # 임시 계산, 10 초과 시 추가 안 함
        temp_sum = sum(self.items) + item
        if temp_sum > 10:
            print(f'*경고: 비료의 총합이 {temp_sum}개로 10개 초과입니다. 비료를 추가하지 않습니다.')
            return

        # 문제없으면 추가
        self.items.append(item)
        print(f'비료 {item}개 추가 완료.')

    # 비료 제거(pop)
    def pop(self):
        if self.empty():
            print('비료가 비어있습니다. 제거할 비료가 없습니다.')
            return None

        # 삭제할거여?
        confirm = input(f'마지막 비료를 빼시겠습니까? (y/n): ')
        if confirm.lower() == 'y':
            item = self.items.pop()
            print(f'비료 {item}개 제거 완료.')
            return item
        else:
            print('제거 취소.')
            return None

    # 마지막 비료 개수 확인(peek)
    def peek(self):
        if self.empty():
            print('비료가 비어있습니다. 확인할 비료가 없습니다.')
            return None

        # 확인 할 건가?
        confirm = input(f'마지막에 추가한 비료의 개수를 확인하시겠습니까? (y/n): ')
        if confirm.lower() == 'y':
            print(f'마지막에 추가한 비료의 개수는 {self.items[-1]}개 입니다.')
            return self.items[-1]
        else:
            print('확인 취소.')
            return None

    # 비료통 비었는지 확인(empty)
    def empty(self):
        return len(self.items) == 0

    # 비료통 상태(display)
    def display_stack(self):
        confirm = input('현재 채워진 비료 상태를 확인하시겠습니까? (y/n): ')
        if confirm.lower() == 'y':
            if self.empty():
                print('[빈 비료통]')
            else:
                print('비료 상태 (아래 -> 위):')
                for index, item in enumerate(self.items):
                    print(f'{index + 1}: {item}개')
            print('-' * 30)
        else:
            print('확인 취소.')

stack = Stack()

while True:
    print('\n[메뉴]')
    print('1. 비료 추가(push)')
    print('2. 비료 제거(pop)')
    print('3. 마지막 비료 개수 확인(peek)')
    print('4. 전체 보기(display)')
    print('5. 종료(exit)')
    choice = input('원하는 작업을 선택하세요: ')

    if choice == '1':
        num = input('추가할 숫자를 입력하세요: ')
        stack.push(num)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.peek()
    elif choice == '4':
        stack.display_stack()
    elif choice == '5':
        print('프로그램을 종료합니다.')
        break
    else:
        print('잘못된 입력입니다. 다시 시도하세요.')
