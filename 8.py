
(left, op, right) = input().split()

try:
    left = float(left)
except Exception:
    print("Неверное значение левого операнда")
    exit()

try:
    right = float(right)
except Exception:
    print("Неверное значение правого операнда")
    exit()

if op == '+':
    print(left + right)
elif op == '-':
    print(left - right)
elif op == '*':
    print(left * right)
elif op == '/':
    print(left / right)
else:
    print("Неверная операция")
