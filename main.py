

class Stack:

    def __init__(self):
        self.items = []

    def print_result(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            print(f" Результат функции {func.__name__} равен {result}")
            return result

        return wrapper

    @print_result
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    @print_result
    def push(self, item):
        self.items.append(item)

    @print_result
    def pop_item(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    @print_result
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    @print_result
    def size(self):
        return len(self.items)

def is_balanced(expression):
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or stack.peek() != bracket_pairs[char]:
                return "Несбалансированно"
            stack.pop_item()

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"

if __name__ == "__main__":
    input_expression = input("Введите строку со скобками: ")
    result = is_balanced(input_expression)
    print(result)









    # stack.is_empty()
    # stack.push(67)
    # stack.is_empty()
    # stack.peek()
    # stack.size()
    # stack.pop_item()
    # stack.size()
    # stack.push(88)
    # stack.size()