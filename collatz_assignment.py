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
except:
    print("enter a integer")
while(True):
    number = collatz(number)
    if number == 1 or number == 0:
        break
