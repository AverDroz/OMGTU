def main_menu():
    while True:
        print("\nМеню:")
        print("1. Автор")
        print("2. Посчитать правую польскую запись")
        print("3. Проверка на правильность скобок")
        print("4. Выход")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            show_author()
        elif choice == '2':
            calculate_rpn()
        elif choice == '3':
            check_brackets()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

def show_author():
    print("\nАвтор: Бухинник Дмитрий Евгеньевич")
    input("Нажмите Enter для возврата в меню.")

def calculate_rpn():
    import operator

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    def evaluate_rpn(expression):
        stack = []
        for token in expression.split():
            if token in ops:
                if len(stack) < 2:
                    return "Ошибка: недостаточно операндов."
                b, a = stack.pop(), stack.pop()
                if token == '/' and b == 0:
                    return "Ошибка: деление на ноль."
                stack.append(ops[token](a, b))
            else:
                try:
                    stack.append(float(token))
                except ValueError:
                    return "Ошибка: некорректное значение."
        if len(stack) != 1:
            return "Ошибка: некорректное выражение."
        return stack[0]

    expression = input("\nВведите правую польскую запись (через пробел): ")
    result = evaluate_rpn(expression)
    print(f"Результат: {result}")
    input("Нажмите Enter для возврата в меню.")

def check_brackets():
    def is_balanced(expression):
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for char in expression:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    return False
        return not stack

    expression = input("\nВведите выражение для проверки скобок: ")
    if is_balanced(expression):
        print("Скобки расставлены правильно.")
    else:
        print("Скобки расставлены неправильно.")
    input("Нажмите Enter для возврата в меню.")

if __name__ == "__main__":
    main_menu()
