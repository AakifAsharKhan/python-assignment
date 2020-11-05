def collatz(number):
    if (number % 2 == 0):
        number = number // 2
        print(number)
        return int(number)
    elif (number % 2 == 1):
        number = 3 * number + 1
        print(number)
        return int(number)
    else:
        return number
try:
    number = int(input("Enter the integer"))
    some_number = number
except:
    print("enter a integer")
while(True):
    some_number = collatz(some_number)
    if some_number == 1:
        break
