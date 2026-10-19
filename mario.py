
while True:
    try:
        height = int(input("შეიყვანეთ პირამიდის სიმაღლე (1-8): "))

        if 1 <= height <= 8:
            break
        else:
            print("გთხოვთ შეიყვანოთ რიცხვი 1-დან 8-ის ჩათვლით.")

    except ValueError:
        print("გთხოვთ შეიყვანოთ მთელი რიცხვი.")

for row in range(1, height + 1):

    for space in range(height - row):
        print(" ", end="")

    for block in range(row):
        print("#", end="")

    print()
