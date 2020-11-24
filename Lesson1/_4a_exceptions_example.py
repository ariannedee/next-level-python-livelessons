try:
    int(input("Enter a number: "))
    print('Good number!')
except ValueError as e:
    print("Not a valid number")
    print(e)


print('Got here')
