
total = 0
count = 0
minimum = None
maximum = None

while True:
    user_input = input("შეიყვანეთ რიცხვი ან 'stop' დასასრულებლად: ")

    if user_input.lower() == "stop":
        break

    try:
        number = float(user_input)

        total += number
        count += 1

        if minimum is None or number < minimum:
            minimum = number

        if maximum is None or number > maximum:
            maximum = number

    except ValueError:
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი ან 'stop'")

print("\nშედეგები:")
print("რიცხვების ჯამი:", total)
print("რიცხვების რაოდენობა:", count)

if count > 0:
    print("მაქსიმალური რიცხვი:", maximum)
    print("მინიმალური რიცხვი:", minimum)
else:
    print("რიცხვები არ შეგიყვანიათ.")
