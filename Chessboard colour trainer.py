import random

COLUMNS = ["A","B","C","D","E","F","G","H"]
ROWS = ["1","2","3","4","5","6","7","8"] 

run = True

while run:
    col_num , row_num = random.randint(0,7) , random.randint(0,7)
    colour = "D" if int(col_num + row_num) % 2 == 0 else "L"
    square_to_try = str(COLUMNS[col_num] + ROWS[row_num])
    print("Square: ", square_to_try)
    attempt = str(input("Enter L if the square is light and D if the square is dark.\n"))
    if attempt.upper() == colour:
        print("Correct\n")
    elif attempt.upper() not in ("L", "D"):
        print("Invalid colour\n")
    else:
        print("Wrong\n")
