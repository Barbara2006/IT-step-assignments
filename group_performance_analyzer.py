
scores = []

while True:
    user_input = input("შეიყვანეთ სტუდენტის ქულა (ან 'stop' დასასრულებლად): ")

    if user_input.lower() == "stop":
        break

    try:
        score = float(user_input)

        if 0 <= score <= 10:
            scores.append(score)
        else:
            print("ქულა უნდა იყოს 0-დან 10-მდე.")

    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი რიცხვი ან 'stop'")

if len(scores) > 0:
    print(f"\nმინიმალური ქულა: {min(scores)}")
    print(f"მაქსიმალური ქულა: {max(scores)}")
    print(f"საშუალო ქულა: {sum(scores) / len(scores):.2f}")

    print("\nქულები ზრდადობით:", sorted(scores))

    print("\nთითოეული ქულის გამეორების რაოდენობა:")
    for score in sorted(set(scores)):
        print(f"{score} — {scores.count(score)}-ჯერ")
else:
    print("ქულები არ არის შეყვანილი.")
