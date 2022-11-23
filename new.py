def add(num1, num2):
    addition = num1+num2
    return addition


def sub(num1, num2):
    subtract = num1-num2
    return subtract


def multiple(num1, num2):
    multiply = num1*num2
    return multiply


first_num = int(input("enter the first number:"))
second_num = int(input("enter second number:"))

print("1. Add\n2. Subtract\n3. Multiply")
choice = input("enter your operation:")2

if choice == 1:
    answer = add(first_num, second_num)
elif choice == 2:
    answer = sub(first_num, second_num)
else :
    answer = multiple(first_num,second_num)
print(answer)



