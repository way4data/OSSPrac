# 스택 자료 구조 정의
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# 연산자 우선순위 설정
def precedence(op):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    return precedence.get(op, 0)

# infix 식을 postfix 식으로 변환
def infix_to_postfix(infix):
    postfix = []
    stack = Stack()

    for token in infix:
        if token.isalnum():
            postfix.append(token)
            # postfix.append(' ')
        elif token in "+-*/^":
            while (not stack.is_empty() and
                   precedence(token) <= precedence(stack.peek())):
                postfix.append(stack.pop())
                # postfix.append(' ')
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while (not stack.is_empty() and stack.peek() != '('):
                postfix.append(stack.pop())
                # postfix.append(' ')
            stack.pop()  # '('를 스택에서 제거

    while not stack.is_empty():
        postfix.append(stack.pop())
        # postfix.append(' ')

    return ''.join(postfix)

"""
# 사용자 입력 받기
infix_expression = input("Infix 형식의 사칙연산식을 입력하세요: ")

# infix를 공백 없이 문자열 리스트로 분할
infix_expression = ''.join(infix_expression.split())

postfix_expression = infix_to_postfix(infix_expression)
print("Postfix 형식으로 변환된 식:", postfix_expression)

"""# 스택 자료 구조 정의
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# 연산자 우선순위 설정
def precedence(op):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    return precedence.get(op, 0)

# infix 식을 postfix 식으로 변환
def infix_to_postfix(infix):
    postfix = []
    stack = Stack()

    operators = "+-*/^"
    for token in infix:
        if token.isalnum():
            postfix.append(token)
        elif token in operators:
            while (not stack.is_empty() and
                   precedence(token) <= precedence(stack.peek()) and
                   stack.peek() in operators):
                postfix.append(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while (not stack.is_empty() and stack.peek() != '('):
                postfix.append(stack.pop())
            stack.pop()  # '('를 스택에서 제거

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)

"""
# 사용자 입력 받기
infix_expression = input("Infix 형식의 사칙연산식을 입력하세요: ")

postfix_expression = infix_to_postfix(infix_expression)
print("Postfix 형식으로 변환된 식:", postfix_expression)
"""
