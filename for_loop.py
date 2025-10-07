rows = input("Enter number of rows: ")
columns = input("Enter number of columns: ")
symbol = input("Enter a symbol to use: ")



for i in range(int(rows)):
    for j in range(int(columns)):
        print(symbol, end="")
    print()